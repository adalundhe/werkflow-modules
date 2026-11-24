import asyncio
import functools
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any, List, Optional, Union
from urllib.parse import quote, urlparse, urlunparse

from werkflow_core import Module
from werkflow_core.exceptions import MissingModuleError
from werkflow_shell import Shell
from werkflow_system import System

try:
    from git import Head, RemoteReference
    from git.remote import Remote
    from git.repo import Repo
    module_enabled = True
except ImportError:
    module_enabled = False
    Head = None  # type: ignore[assignment,misc]
    RemoteReference = None  # type: ignore[assignment,misc]
    Repo = None  # type: ignore[assignment,misc]
    Remote = None  # type: ignore[assignment,misc]


class Git(Module):
    module_enabled = module_enabled
    dependencies = ['gitpython', 'werkflow-shell', 'werkflow-system']

    def __init__(self) -> None:
        super().__init__()
        if not self.module_enabled or Repo is None:
            raise MissingModuleError(self)

        self._system = System()
        self._shell = Shell()

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self.repo: Optional[Repo] = None
        self.remote: Optional[Remote] = None
        self.branch: Optional[Head] = None
        self.git: Optional[Any] = None

    def _ensure_enabled(self) -> None:
        if not self.module_enabled or Repo is None:
            raise MissingModuleError(self)

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    def _close_repo(self) -> None:
        if self.repo is not None:
            self.repo.close()
            self.repo = None
            self.remote = None
            self.branch = None
            self.git = None

    def _has_commits(self) -> bool:
        if self.repo is None:
            return False
        return bool(self.repo.head.is_valid())

    def _get_active_branch(self) -> Optional[Head]:
        if self.repo is None:
            return None
        try:
            if self.repo.head.is_detached:
                return None
            return self.repo.active_branch
        except (TypeError, ValueError):
            return None

    def _get_current_branch_name(self) -> Optional[str]:
        active_branch = self._get_active_branch()
        if active_branch is None:
            return None
        return active_branch.name

    def _resolve_branch_name(self, branch: Optional[str]) -> str:
        if branch is not None:
            return branch
        if self.branch is not None:
            return self.branch.name
        current_branch = self._get_current_branch_name()
        if current_branch is not None:
            return current_branch
        return 'main'

    def _find_remote_ref(
        self,
        remote_name: Optional[str],
        branch: str,
    ) -> Optional[RemoteReference]:
        if self.repo is None or remote_name is None:
            return None
        remote_names = {r.name for r in self.repo.remotes}
        if remote_name not in remote_names:
            return None
        remote_obj = self.repo.remotes[remote_name]
        expected_full = f'{remote_name}/{branch}'
        for ref in remote_obj.refs:
            if ref.remote_head == branch or ref.name == expected_full:
                return ref
        return None

    async def reinitialize(
        self,
        path: Optional[str] = None,
        remote: Optional[str] = None,
        branch: Optional[str] = None,
    ) -> None:
        self._ensure_enabled()
        assert Repo is not None
        loop = self._get_loop()

        if path is None:
            resolved_path = await self._shell.get_current_directory()
        else:
            resolved_path = await self._shell.to_absolute_path(path)

        self._close_repo()

        self.repo = await loop.run_in_executor(
            self._executor,
            functools.partial(Repo, resolved_path),
        )
        self.git = self.repo.git

        if branch is not None:
            if self._has_commits():
                def _get_or_create_branch() -> Head:
                    assert self.repo is not None
                    if branch in self.repo.heads:
                        return self.repo.heads[branch]
                    return self.repo.create_head(branch)

                self.branch = await loop.run_in_executor(
                    self._executor,
                    _get_or_create_branch,
                )
            else:
                self.branch = self._get_active_branch()
        else:
            self.branch = self._get_active_branch()

        if remote is not None:
            remote_names = {r.name for r in self.repo.remotes}
            if remote in remote_names:
                self.remote = await loop.run_in_executor(
                    self._executor,
                    functools.partial(self.repo.remote, remote),
                )
            else:
                self.remote = None

    async def check_if_repo_exists(
        self,
        path: Optional[str] = None,
    ) -> bool:
        self._ensure_enabled()
        if path is None:
            resolved_path = await self._shell.get_current_directory()
        else:
            resolved_path = await self._shell.to_absolute_path(path)

        git_path = os.path.join(resolved_path, '.git')
        return await self._shell.check_path_exists(
            git_path,
            silent=True,
        )

    async def check_remote_is_set(self) -> bool:
        self._ensure_enabled()
        if Repo is not None and isinstance(self.repo, Repo):
            return len(self.repo.remotes) > 0
        return False

    async def init(
        self,
        path: str,
        branch: str = 'main',
        gitignore_items: Optional[List[str]] = None,
        gitignore_filepath: Optional[str] = None,
    ) -> None:
        self._ensure_enabled()
        assert Repo is not None
        loop = self._get_loop()

        absolute_path = await self._shell.to_absolute_path(path)
        git_repo_exists = await self.check_if_repo_exists(path=absolute_path)

        if not git_repo_exists:
            self._close_repo()

            def _init_repo() -> Repo:
                assert Repo is not None
                try:
                    return Repo.init(absolute_path, initial_branch=branch)
                except Exception:
                    repo = Repo.init(absolute_path)
                    repo.git.symbolic_ref('HEAD', f'refs/heads/{branch}')
                    return repo

            self.repo = await loop.run_in_executor(
                self._executor,
                _init_repo,
            )
            self.git = self.repo.git
            self.branch = self._get_active_branch()

            await self.set_gitignore(
                gitignore_items if gitignore_items is not None else [],
                gitignore_filepath=gitignore_filepath,
                path=absolute_path,
            )

            await self.commit(
                f'Initialized new repo at - {absolute_path}',
                branch=branch,
                initial_commit=True,
            )

            self.branch = self._get_active_branch()
            self.git = self.repo.git
        else:
            await self.reinitialize(path=absolute_path)

    async def checkout(
        self,
        branch: str,
        remote: Optional[str] = 'origin',
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize(remote=remote)

        assert self.repo is not None

        if not self._has_commits():
            await loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.symbolic_ref,
                    'HEAD',
                    f'refs/heads/{branch}',
                ),
            )
            self.branch = self._get_active_branch()
            return

        def _checkout_branch() -> Head:
            assert self.repo is not None
            remote_ref = self._find_remote_ref(remote, branch)

            if branch in self.repo.heads:
                head = self.repo.heads[branch]
                if remote_ref is not None and head.tracking_branch() is None:
                    head.set_tracking_branch(remote_ref)
                head.checkout()
                return head

            if remote_ref is not None:
                head = self.repo.create_head(branch, remote_ref)
                head.set_tracking_branch(remote_ref)
                head.checkout()
                return head

            head = self.repo.create_head(branch)
            head.checkout()
            return head

        self.branch = await loop.run_in_executor(
            self._executor,
            _checkout_branch,
        )

    async def set_gitignore(
        self,
        gitignore_items: List[str],
        gitignore_filepath: Optional[str] = None,
        path: Optional[str] = None,
    ) -> None:
        self._ensure_enabled()

        if gitignore_filepath is None:
            if path is not None:
                target_directory = await self._shell.to_absolute_path(path)
            elif self.repo is not None and self.repo.working_tree_dir is not None:
                target_directory = str(self.repo.working_tree_dir)
            else:
                target_directory = await self._shell.get_current_directory()

            gitignore_filepath = os.path.join(
                target_directory,
                '.gitignore',
            )
        else:
            gitignore_filepath = await self._shell.to_absolute_path(gitignore_filepath)

        file_exists = await self._shell.check_path_exists(gitignore_filepath)

        if len(gitignore_items) > 0 and not file_exists:
            gitignore_text = '\n'.join(gitignore_items) + '\n'
            await self._shell.pipe_to_file(
                gitignore_filepath,
                gitignore_text,
                overwrite=True,
                silent=True,
            )
        elif not file_exists:
            await self._shell.touch(
                gitignore_filepath,
                overwrite=True,
                silent=True,
            )

        await self.add(
            gitignore_filepath,
            initial_commit=True,
        )

    async def clone(
        self,
        url: str,
        path: str,
        remote: str = 'origin',
        branch: Optional[str] = 'main',
    ) -> None:
        self._ensure_enabled()
        assert Repo is not None
        loop = self._get_loop()

        absolute_path = await self._shell.to_absolute_path(path)
        self._close_repo()

        self.repo = await loop.run_in_executor(
            self._executor,
            functools.partial(Repo.clone_from, url, absolute_path),
        )
        self.git = self.repo.git

        remote_names = {r.name for r in self.repo.remotes}
        if remote in remote_names:
            self.remote = await loop.run_in_executor(
                self._executor,
                functools.partial(self.repo.remote, name=remote),
            )
        else:
            self.remote = None

        self.branch = self._get_active_branch()

        if branch is not None and branch != self._get_current_branch_name():
            await self.checkout(branch, remote=remote)

    async def fetch(
        self,
        remote: str = 'origin',
        branch: Optional[str] = None,
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize(remote=remote)

        if self.remote is None or self.remote.name != remote:
            await self.reinitialize_remote(remote=remote)

        assert self.remote is not None
        await loop.run_in_executor(
            self._executor,
            self.remote.fetch,
        )

        if branch is not None and branch != self._get_current_branch_name():
            await self.checkout(branch, remote=remote)

    async def reinitialize_remote(
        self,
        remote: str = 'origin',
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize()

        assert self.repo is not None
        self.remote = await loop.run_in_executor(
            self._executor,
            functools.partial(self.repo.remote, remote),
        )

    async def set_remote(
        self,
        url: str,
        remote: str = 'origin',
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> str:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize()

        assert self.repo is not None

        if username and password:
            parsed_repo_url = urlparse(url)
            encoded_username = quote(username, safe='')
            encoded_password = quote(password, safe='')
            host = parsed_repo_url.hostname or ''
            if ':' in host and not host.startswith('['):
                host = f'[{host}]'
            port_part = (
                f':{parsed_repo_url.port}'
                if parsed_repo_url.port is not None
                else ''
            )
            netloc = f'{encoded_username}:{encoded_password}@{host}{port_part}'
            url = urlunparse((
                parsed_repo_url.scheme,
                netloc,
                parsed_repo_url.path,
                parsed_repo_url.params,
                parsed_repo_url.query,
                parsed_repo_url.fragment,
            ))

        remote_names = [existing.name for existing in self.repo.remotes]

        if remote not in remote_names:
            await loop.run_in_executor(
                self._executor,
                functools.partial(self.repo.create_remote, remote, url),
            )

        self.remote = await loop.run_in_executor(
            self._executor,
            functools.partial(self.repo.remote, remote),
        )

        await loop.run_in_executor(
            self._executor,
            functools.partial(self.remote.set_url, url),
        )

        return url

    def _normalize_repo_paths(
        self,
        filepaths: List[str],
    ) -> List[str]:
        assert self.repo is not None
        working_tree = self.repo.working_tree_dir
        if working_tree is None:
            return filepaths

        real_root = os.path.realpath(str(working_tree))
        normalized: List[str] = []
        for filepath in filepaths:
            if os.path.isabs(filepath):
                real_file = os.path.realpath(filepath)
                try:
                    if os.path.commonpath([real_root, real_file]) == real_root:
                        normalized.append(os.path.relpath(real_file, real_root))
                        continue
                except ValueError:
                    pass
            normalized.append(filepath)
        return normalized

    async def add(
        self,
        filepath: Optional[Union[str, List[str]]] = None,
        branch: Optional[str] = None,
        commit_all: bool = False,
        initial_commit: bool = False,
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize()

        assert self.repo is not None

        resolved_branch = self._resolve_branch_name(branch)
        if resolved_branch != self._get_current_branch_name():
            await self.checkout(resolved_branch)

        if commit_all:
            await loop.run_in_executor(
                self._executor,
                functools.partial(self.repo.git.add, A=True),
            )
        elif filepath is not None:
            raw_paths = [filepath] if isinstance(filepath, str) else list(filepath)
            normalized_paths = self._normalize_repo_paths(raw_paths)
            await loop.run_in_executor(
                self._executor,
                functools.partial(self.repo.index.add, normalized_paths),
            )
        else:
            raise ValueError(
                "Either 'filepath' must be provided or 'commit_all=True'."
            )

    async def commit(
        self,
        message: str,
        branch: Optional[str] = None,
        remote: str = 'origin',
        initial_commit: bool = False,
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize(branch=branch)

        assert self.repo is not None

        resolved_branch = self._resolve_branch_name(branch)
        if resolved_branch != self._get_current_branch_name():
            await self.checkout(resolved_branch, remote=remote)

        def _commit_if_needed() -> None:
            assert self.repo is not None
            if not self._has_commits():
                if len(self.repo.index.entries) == 0:
                    return
            else:
                has_staged = bool(self.repo.index.diff('HEAD'))
                if not has_staged:
                    return
            self.repo.git.commit('-m', message)

        await loop.run_in_executor(self._executor, _commit_if_needed)
        self.branch = self._get_active_branch()

    async def pull(
        self,
        branch: Optional[str] = None,
        remote: str = 'origin',
        rebase: bool = True,
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize(remote=remote)

        resolved_branch = self._resolve_branch_name(branch)
        if resolved_branch != self._get_current_branch_name():
            await self.checkout(resolved_branch, remote=remote)

        if self.remote is None or self.remote.name != remote:
            await self.reinitialize_remote(remote=remote)

        def _pull_if_remote_branch_exists() -> None:
            assert self.remote is not None
            self.remote.fetch()
            remote_heads = {ref.remote_head for ref in self.remote.refs}
            remote_ref_names = {ref.name for ref in self.remote.refs}
            if (
                resolved_branch in remote_heads
                or f'{remote}/{resolved_branch}' in remote_ref_names
            ):
                self.remote.pull(resolved_branch, rebase=rebase)

        await loop.run_in_executor(self._executor, _pull_if_remote_branch_exists)

    async def push(
        self,
        branch: Optional[str] = None,
        remote: str = 'origin',
    ) -> None:
        self._ensure_enabled()
        loop = self._get_loop()

        if self.repo is None:
            await self.reinitialize(remote=remote)

        assert self.repo is not None

        resolved_branch = self._resolve_branch_name(branch)
        if resolved_branch != self._get_current_branch_name():
            await self.checkout(resolved_branch, remote=remote)

        if self.remote is None or self.remote.name != remote:
            await self.reinitialize_remote(remote=remote)

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                self.repo.git.push,
                '--set-upstream',
                remote,
                resolved_branch,
            ),
        )

    async def close(self) -> None:
        self._close_repo()
        await self._shell.close()
        await self._system.close()
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        self._close_repo()
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown(wait=False, cancel_futures=True)
