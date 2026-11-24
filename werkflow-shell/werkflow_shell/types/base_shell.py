import abc
import asyncio
import functools
import os
import pathlib
import shlex
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from typing import BinaryIO, Dict, List, Optional, TextIO, Union, overload, Literal

from werkflow_system import System
from .shell_type import ShellType


class BaseShell(abc.ABC):
    shell_type: ShellType = ShellType.SH

    def __init__(self, system: Optional[System] = None) -> None:
        self.last_command: Optional[str] = None
        self.env: Dict[str, str] = os.environ.copy()
        self._system: System = system if system is not None else System()
        self._home: str = str(self._system.users.home)
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self.silent: bool = False
        self.shell_executable: str = self._detect_executable()
        self.envfile_name: str = self._default_envfile_name()
        self.envfile_path: str = self._default_envfile_path()

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    def _resolve_silent(self, silent: Optional[bool]) -> bool:
        return self.silent if silent is None else silent

    @abc.abstractmethod
    def _detect_executable(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def _default_envfile_name(self) -> str:
        raise NotImplementedError()

    def _default_envfile_path(self) -> str:
        return os.path.join(self._home, self.envfile_name)

    @abc.abstractmethod
    def _build_shell_command(self, command: str) -> List[str]:
        raise NotImplementedError()

    def _split_command(self, command: str) -> List[str]:
        return shlex.split(command, posix=True)

    @abc.abstractmethod
    def _format_envfile_entry(
        self,
        variable_name: str,
        variable_value: str,
    ) -> str:
        raise NotImplementedError()

    def path_is_file(self, path: str) -> bool:
        expanded = self._expand_path_sync(path)
        if os.path.exists(expanded):
            return os.path.isfile(expanded)
        return len(pathlib.Path(expanded).suffix) > 0

    def path_is_directory(self, path: str) -> bool:
        expanded = self._expand_path_sync(path)
        if os.path.exists(expanded):
            return os.path.isdir(expanded)
        return len(pathlib.Path(expanded).suffix) == 0

    def _expand_path_sync(self, filepath: str) -> str:
        if not filepath:
            return filepath

        if filepath == '~':
            return self._home

        if filepath.startswith('~/') or filepath.startswith('~\\'):
            return os.path.join(self._home, filepath[2:])

        if filepath.startswith('~'):
            return os.path.expanduser(filepath)

        return filepath

    async def which(self, executable: str) -> Optional[str]:
        loop = self._get_loop()
        search_path = self.env.get('PATH') or os.environ.get('PATH')
        return await loop.run_in_executor(
            self._executor,
            functools.partial(shutil.which, executable, path=search_path),
        )

    async def get_envar(
        self,
        envar_name: str,
        default: Optional[str] = None,
    ) -> Optional[str]:
        if envar_name in self.env:
            return self.env[envar_name]

        loop = self._get_loop()
        return await loop.run_in_executor(
            self._executor,
            functools.partial(os.getenv, envar_name, default),
        )

    async def set_envar(
        self,
        envar_name: str,
        envar_value: Union[str, bytes],
    ) -> None:
        value = (
            envar_value.decode('utf-8')
            if isinstance(envar_value, bytes)
            else str(envar_value)
        )
        self.env[envar_name] = value

        loop = self._get_loop()

        def _set() -> None:
            os.environ[envar_name] = value

        await loop.run_in_executor(self._executor, _set)

    async def check_if_is_file(self, filepath: str) -> bool:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)
        return await loop.run_in_executor(
            self._executor,
            functools.partial(os.path.isfile, absolute_path),
        )

    async def check_if_is_directory(self, filepath: str) -> bool:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)
        return await loop.run_in_executor(
            self._executor,
            functools.partial(os.path.isdir, absolute_path),
        )

    async def check_file_access(
        self,
        filepath: str,
        permissions: int,
    ) -> bool:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)
        return await loop.run_in_executor(
            self._executor,
            functools.partial(os.access, absolute_path, permissions),
        )

    async def to_absolute_path(self, filepath: str) -> str:
        loop = self._get_loop()
        if not filepath:
            return await self.get_current_directory()

        has_trailing_sep = len(filepath) > 1 and filepath[-1] in ('/', '\\')
        expanded = self._expand_path_sync(filepath)
        path = pathlib.Path(expanded)

        resolved_path = await loop.run_in_executor(
            self._executor,
            path.resolve,
        )

        absolute_path = str(resolved_path)
        if has_trailing_sep and not absolute_path.endswith(os.sep):
            absolute_path = f'{absolute_path}{os.sep}'

        return absolute_path

    async def to_relative_path(
        self,
        base_path: str,
        absolute_path: str,
    ) -> str:
        loop = self._get_loop()

        def _relpath() -> str:
            try:
                return os.path.relpath(absolute_path, base_path)
            except ValueError:
                return os.path.abspath(absolute_path)

        return await loop.run_in_executor(self._executor, _relpath)

    async def get_current_directory(self) -> str:
        loop = self._get_loop()
        return await loop.run_in_executor(self._executor, os.getcwd)

    async def change_directory(self, directory_path: str) -> None:
        absolute_path = await self.to_absolute_path(directory_path)
        loop = self._get_loop()
        await loop.run_in_executor(
            self._executor,
            functools.partial(os.chdir, absolute_path),
        )

    def _merged_env(self, env: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        merged = {**os.environ, **self.env}
        if env:
            for key, value in env.items():
                merged[key] = str(value)
        return merged

    def _update_env_from_mapping(self, captured: Dict[str, str]) -> None:
        for key, value in captured.items():
            if not key:
                continue
            self.env[key] = value
            os.environ[key] = value

    @abc.abstractmethod
    async def assume_admin(
        self,
        password: Optional[str] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        raise NotImplementedError()

    async def run(
        self,
        command: str,
        command_input: Optional[str] = None,
        path: Optional[str] = None,
        env: Optional[Dict[str, str]] = None,
        as_shell: bool = False,
        silent: Optional[bool] = None,
        timeout: Optional[float] = None,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        use_silent = self._resolve_silent(silent)
        output_pipe = subprocess.PIPE if use_silent else None
        loop = self._get_loop()

        process_command: List[str] = (
            self._build_shell_command(command)
            if as_shell
            else self._split_command(command)
        )

        self.last_command = command
        merged_env = self._merged_env(env)

        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                subprocess.run,
                process_command,
                cwd=path,
                stdout=output_pipe,
                stderr=output_pipe,
                text=True,
                input=command_input,
                shell=False,
                timeout=timeout,
                check=check,
                env=merged_env,
            ),
        )

    @abc.abstractmethod
    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        raise NotImplementedError()

    @abc.abstractmethod
    async def source(
        self,
        filepath: Optional[str] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        raise NotImplementedError()

    async def copy(
        self,
        source_directory: str,
        destination_directory: str,
        recursive: bool = False,
        silent: Optional[bool] = None,
    ) -> None:
        loop = self._get_loop()
        src = await self.to_absolute_path(source_directory)
        dst = await self.to_absolute_path(destination_directory)

        def _copy() -> None:
            if os.path.isdir(src):
                if not recursive:
                    raise IsADirectoryError(
                        f"Cannot copy directory '{src}' without recursive=True."
                    )
                target = dst
                if os.path.isdir(dst):
                    target = os.path.join(dst, os.path.basename(src.rstrip('/\\')))
                shutil.copytree(src, target, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

        await loop.run_in_executor(self._executor, _copy)

    async def move(
        self,
        source_directory: str,
        destination_directory: str,
        silent: Optional[bool] = None,
    ) -> None:
        loop = self._get_loop()
        src = await self.to_absolute_path(source_directory)
        dst = await self.to_absolute_path(destination_directory)

        await loop.run_in_executor(
            self._executor,
            functools.partial(shutil.move, src, dst),
        )

    async def append_to_envfile(
        self,
        variable_name: str,
        variable_value: str,
    ) -> None:
        loop = self._get_loop()
        entry = self._format_envfile_entry(variable_name, variable_value)
        parent_dir = os.path.dirname(self.envfile_path)
        if parent_dir:
            await self.create_directory(parent_dir)

        def _append() -> None:
            needs_leading_newline = False
            if os.path.exists(self.envfile_path) and os.path.getsize(self.envfile_path) > 0:
                with open(self.envfile_path, 'rb') as existing:
                    existing.seek(-1, os.SEEK_END)
                    needs_leading_newline = existing.read(1) != b'\n'

            with open(self.envfile_path, 'a', encoding='utf-8') as envfile:
                if needs_leading_newline:
                    envfile.write('\n')
                envfile.write(f'{entry}\n')

        await loop.run_in_executor(self._executor, _append)
        await self.set_envar(variable_name, variable_value)

    async def check_path_exists(self, filepath: str) -> bool:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)
        return await loop.run_in_executor(
            self._executor,
            functools.partial(os.path.exists, absolute_path),
        )

    async def touch(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
    ) -> None:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)

        def _touch() -> None:
            if overwrite or not os.path.exists(absolute_path):
                if is_bytes:
                    with open(absolute_path, 'wb'):
                        pass
                else:
                    with open(absolute_path, 'w', encoding='utf-8'):
                        pass
            else:
                pathlib.Path(absolute_path).touch(exist_ok=True)

        await loop.run_in_executor(self._executor, _touch)

    async def create_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
    ) -> Optional[Union[TextIO, BinaryIO]]:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)
        file_exists = await self.check_path_exists(absolute_path)

        if not file_exists or overwrite:
            if is_bytes:
                return await loop.run_in_executor(
                    self._executor,
                    functools.partial(open, absolute_path, 'wb+'),
                )
            return await loop.run_in_executor(
                self._executor,
                functools.partial(open, absolute_path, 'w+', encoding='utf-8'),
            )
        return None

    async def open_or_create_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
    ) -> Union[TextIO, BinaryIO]:
        absolute_path = await self.to_absolute_path(filepath)

        write_file = await self.create_file(
            absolute_path,
            is_bytes=is_bytes,
            overwrite=overwrite,
        )

        if write_file is None:
            write_file = await self.open_existing_file(
                absolute_path,
                is_bytes=is_bytes,
            )

        return write_file

    async def open_existing_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        write_mode: str = 'a+',
    ) -> Union[TextIO, BinaryIO]:
        loop = self._get_loop()
        mode = write_mode
        if is_bytes and 'b' not in mode:
            mode = f'{mode[0]}b{mode[1:]}'

        absolute_path = await self.to_absolute_path(filepath)
        if 'b' in mode:
            return await loop.run_in_executor(
                self._executor,
                functools.partial(open, absolute_path, mode),
            )
        return await loop.run_in_executor(
            self._executor,
            functools.partial(open, absolute_path, mode, encoding='utf-8'),
        )

    @overload
    async def read_file(self, filepath: str, is_bytes: Literal[False] = False) -> str: ...

    @overload
    async def read_file(self, filepath: str, is_bytes: Literal[True]) -> bytes: ...

    @overload
    async def read_file(self, filepath: str, is_bytes: bool = False) -> Union[str, bytes]: ...

    async def read_file(
        self,
        filepath: str,
        is_bytes: bool = False,
    ) -> Union[str, bytes]:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(filepath)

        def _read() -> Union[str, bytes]:
            if is_bytes:
                with open(absolute_path, 'rb') as file_handle:
                    return file_handle.read()
            with open(absolute_path, 'r', encoding='utf-8') as file_handle:
                return file_handle.read()

        return await loop.run_in_executor(self._executor, _read)

    async def pipe_to_file(
        self,
        filepath: str,
        data: Union[str, bytes],
        overwrite: bool = False,
    ) -> None:
        loop = self._get_loop()
        is_bytes = isinstance(data, bytes)
        absolute_path = await self.to_absolute_path(filepath)

        def _write() -> None:
            if is_bytes:
                mode = 'wb' if overwrite else 'ab'
                with open(absolute_path, mode) as file_handle:
                    file_handle.write(data)
            else:
                mode = 'w' if overwrite else 'a'
                with open(absolute_path, mode, encoding='utf-8') as file_handle:
                    file_handle.write(data)

        await loop.run_in_executor(self._executor, _write)

    async def create_directory(self, directory_path: str) -> None:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(directory_path)
        await loop.run_in_executor(
            self._executor,
            functools.partial(os.makedirs, absolute_path, exist_ok=True),
        )

    async def rm(
        self,
        path: str,
        pattern: Optional[str] = None,
        recurse: bool = False,
    ) -> None:
        loop = self._get_loop()
        absolute_path = await self.to_absolute_path(path)

        def _remove_single(target: pathlib.Path) -> None:
            if not target.exists() and not target.is_symlink():
                return
            if target.is_symlink() or target.is_file():
                target.unlink(missing_ok=True)
            elif target.is_dir():
                shutil.rmtree(target, ignore_errors=False)

        def _rm() -> None:
            target = pathlib.Path(absolute_path)
            if not target.exists() and not target.is_symlink():
                return

            if pattern is not None and target.is_dir():
                iterator = target.rglob(pattern) if recurse else target.glob(pattern)
                matches = sorted(
                    iterator,
                    key=lambda p: len(p.parts),
                    reverse=True,
                )
                for match in matches:
                    _remove_single(match)
            elif recurse and target.is_dir():
                shutil.rmtree(target)
            elif target.is_dir():
                shutil.rmtree(target)
            else:
                _remove_single(target)

        await loop.run_in_executor(self._executor, _rm)

    async def close(self) -> None:
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        self._executor.shutdown(wait=False, cancel_futures=True)
