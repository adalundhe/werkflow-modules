import asyncio
import functools
import os
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional
from urllib.parse import urlparse

from werkflow.modules.base import Module
from werkflow.modules.shell import Shell
from werkflow.modules.system import System

try:
    module_enabled = True
    from git import RemoteReference
    from git.remote import Remote
    from git.repo import Repo

except ImportError:
    module_enabled = False
    RemoteReference=None
    Repo=None
    Remote=None


class Git(Module):
    module_enabled=module_enabled
    dependencies=['gitpython']

    def __init__(self) -> None:
        super().__init__()

        self._system = System()
        self._shell = Shell()

        self._loop: asyncio.AbstractEventLoop = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self.repo: Repo = None
        self.remote: Remote = None
        self.branch = None
        self.git = None

    async def reinitialize(
        self,
        path: str | None = None,
        remote: str=None,
        branch: Optional[str]=None
    ) -> None:
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if path is None:
            path = await self._shell.get_current_directory()
        self.repo = Repo(path)
     
        self.git = self.repo.git

        if branch:
            self.branch = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.create_head,
                    branch
                )
            )

        if remote:
            self.remote = Remote(
                self.repo, 
                remote
            )

            self.remote = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.remote,
                    remote
                )
            )

    async def check_if_repo_exists(
        self,
        path: str | None = None
    ) -> bool:

        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if path is None:
            path = await self._shell.get_current_directory()
        git_path = os.path.join(
            path,
            '.git'
        )

        return await self._shell.check_path_exists(
            git_path,
            silent=True
        )
    
    async def check_remote_is_set(self) -> bool:
        if isinstance(self.repo, Repo):
            return len(self.repo.remotes) > 0


    async def init(
        self,
        path: str,
        branch: str='main',
        gitignore_items: List[str]=[],
        gitignore_filepath: str=None
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        git_repo_exists = await self.check_if_repo_exists()

        if git_repo_exists is False:
       
            self.repo = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    Repo.init,
                    path
                )
            )

            await self.set_gitignore(
                gitignore_items,
                gitignore_filepath=gitignore_filepath
            )

            await self.commit(
                f'Initialized new repo at - {path}',
                initial_commit=True
            )

            self.branch = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.create_head,
                    branch
                )
            )

            self.git = self.repo.git

        else:
            await self.reinitialize()

    async def checkout(
        self,
        branch: str,
        remote: str='origin'
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize(
                branch=branch,
                remote=remote
            )

        try:
            self.branch = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.checkout,
                    branch
                )
            )
            

        except Exception:
            self.branch = await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.checkout,
                    '-b',
                    branch
                )
            )
            
        
        self.branch = await self._loop.run_in_executor(
            self._executor,
            self.repo.create_head,
            branch
        )

        self.repo.head.reference = self.branch

        remote_reference = RemoteReference(
            self.repo, 
            f"refs/remotes/{remote}/{branch}"
        )

        tracking_branch = await self._loop.run_in_executor(
            self._executor,
            functools.partial(    
                self.repo.head.reference.set_tracking_branch,
                remote_reference
            )
        )

        await self._loop.run_in_executor(
            self._executor,
            tracking_branch.checkout
        )


    async def set_gitignore(
        self, 
        gitignore_items: List[str],
        gitignore_filepath: str=None
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if gitignore_filepath is None:
            current_directory = await self._shell.get_current_directory()

            gitignore_filepath = os.path.join(
                current_directory,
                '.gitignore'
            )

        file_exists = await self._shell.check_path_exists(gitignore_filepath)

        if len(gitignore_items) > 0 and file_exists is False:
            
            gitignore_text = '\n'.join(gitignore_items)

            await self._shell.pipe_to_file(
                gitignore_filepath,
                gitignore_text,
                overwrite=True,
                silent=True
            )

        elif file_exists is False:
            await self._shell.touch(
                gitignore_filepath,
                overwrite=True,
                silent=True
            )

        await self.add(
            '.gitignore',
            initial_commit=True
        )

    async def clone(
        self,
        url: str,
        path: str,
        remote: str='origin',
        branch: str='main'
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        self.repo = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                Repo.clone_from,
                url, 
                path
            )
        )

        self.branch = await self._loop.run_in_executor(
            self._executor,
            functools.partial(        
                self.repo.create_head,
                branch
            )
        )

        if branch != self.repo.head.name:
            await self.checkout(branch)

        self.remote = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.repo.remote,
                name=remote
            )
        )

        self.git = self.repo.git

    async def fetch(
        self,
        remote: str='origin',
        branch: str='main'
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize(
                branch=branch,
                remote=remote
            )

        if branch != self.repo.head.name:
            await self.checkout(branch)

        if self.remote is None:
            await self.reinitialize_remote(
                remote=remote
            )

        await self._loop.run_in_executor(
            self._executor,
            self.remote.fetch
        )

    async def reinitialize_remote(
        self,
        remote: str='origin'
    ):
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize()
        
        self.remote = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.repo.remote,
                remote
            )
        )

    async def set_remote(
        self,
        url: str,
        remote: str='origin',
        username: str=None,
        password: str=None
    ) -> str:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize()

        if username and password:
            parsed_repo_url = urlparse(url)
            url = ''.join([
                f'{parsed_repo_url.scheme}://',
                f'{username}:{password}',
                f'@{parsed_repo_url.hostname}',
                f'{parsed_repo_url.path}'
            ])

        remote_names = [
            remote.name for remote in self.repo.remotes
        ]
        
        if remote not in remote_names:
            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.create_remote,
                    remote,
                    url
                )
            )

        self.remote = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.repo.remote,
                remote
            )
        )

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.remote.set_url,
                url
            )
        )

        return url

    async def add(
        self,
        filepath: str=None,
        branch: Optional[str]=None,
        commit_all: bool=False,
        initial_commit: bool=False
    ):
        
        if branch is None and self.branch:
            branch = self.branch.name

        elif branch is None:
            branch = 'main'

        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize()

        if branch != self.repo.head.name:
            await self.checkout(branch)

        if commit_all:
            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.add,
                    A=commit_all
                )
            )

        else:
            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.index.add,
                    filepath
                )
            )

    async def commit(
        self,
        message: str,
        branch: Optional[str]=None,
        remote: str='origin',
        initial_commit: bool=False
    ):
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if branch is None and self.branch:
            branch = self.branch.name

        elif branch is None:
            branch = 'main'

        if self.repo is None:
            await self.reinitialize(
                branch=branch,
                remote=remote
            )

        if branch != self.repo.head.name:
            await self.checkout(branch)

        if self.remote is None:
            await self.reinitialize_remote(
                remote=remote
            )

        try:
            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.commit,
                    '-m',
                    message
                )
            )

        except Exception as commit_error:
            
            traceback_message = traceback.format_exc()

            if 'working tree clean' not in traceback_message:
                raise commit_error
        
    async def pull(
        self,
        branch: Optional[str]=None,
        remote: str='origin',
        rebase: bool=True
    ):
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize()

        if branch is None and self.branch.name:
            branch = self.branch.name

        elif branch is None:
            branch = 'main'

        if self.repo is None:
            await self.reinitialize(
                branch=branch,
                remote=remote
            )

        if branch != self.repo.head.name:
            await self.checkout(branch)

        if self.remote is None:
            await self.reinitialize_remote(
                remote=remote
            )

        remote_refs = [
            ref.name for ref in self.remote.refs
        ]

        if branch in remote_refs:
            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.remote.pull,
                    branch,
                    rebase=rebase
                )
            )

    async def push(
        self,
        branch: Optional[str]=None,
        remote: str='origin'
    ):
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.repo is None:
            await self.reinitialize()

        if branch is None and self.branch:
            branch = self.branch.name

        elif branch is None:
            branch = 'main'

        if branch != self.repo.head.name:
            await self.checkout(branch)

        if self.remote is None:
            await self.reinitialize_remote(
                remote=remote
            )

        try:

            await self._loop.run_in_executor(
                self._executor,
                functools.partial(
                    self.repo.git.push,
                    '--set-upstream',
                    remote,
                    self.branch
                )
            )

        except Exception:
            pass

    async def close(self):
        await self._shell.close()
        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown()