import subprocess
from typing import BinaryIO, Dict, Optional, TextIO, Type, Union

from werkflow_core import Module
from werkflow_system import OperatingSystemType, System
from .types import (
    BaseShell,
    BashShell,
    CmdShell,
    FishShell,
    POSIXShell,
    PowerShellShell,
    ShShell,
    ShellResolver,
    ShellType,
    ZSHShell,
)


class Shell(Module):
    dependencies = ['werkflow-system']

    def __init__(self, shell_type: Optional[ShellType] = None) -> None:
        super().__init__()
        self._system = System()

        self._shell_types: Dict[OperatingSystemType, Type[BaseShell]] = {
            OperatingSystemType.MAC_OS: ZSHShell,
            OperatingSystemType.LINUX: BashShell,
            OperatingSystemType.WINDOWS: PowerShellShell,
        }

        shell_cls = ShellResolver.resolve(self._system, shell_type=shell_type)
        self._shell: BaseShell = shell_cls(system=self._system)

    @property
    def shell_type(self) -> ShellType:
        return self._shell.shell_type

    @property
    def executable(self) -> str:
        return self._shell.shell_executable

    @property
    def os_type(self) -> Optional[OperatingSystemType]:
        return self._system.os.type

    @property
    def system(self) -> System:
        return self._system

    @property
    def env(self) -> Dict[str, str]:
        return self._shell.env

    @property
    def envfile_path(self) -> str:
        return self._shell.envfile_path

    def path_is_file(self, path: str) -> bool:
        return self._shell.path_is_file(path)

    def path_is_directory(self, path: str) -> bool:
        return self._shell.path_is_directory(path)

    async def which(self, executable: str) -> Optional[str]:
        return await self._shell.which(executable)

    async def get_envar(
        self,
        envar_name: str,
        default: Optional[str] = None,
    ) -> Optional[str]:
        return await self._shell.get_envar(envar_name, default=default)

    async def set_envar(
        self,
        envar_name: str,
        envar_value: Union[str, bytes],
    ) -> None:
        await self._shell.set_envar(envar_name, envar_value)

    async def check_if_is_file(self, path: str) -> bool:
        return await self._shell.check_if_is_file(path)

    async def check_if_is_directory(self, path: str) -> bool:
        return await self._shell.check_if_is_directory(path)

    async def get_current_directory(self) -> str:
        return await self._shell.get_current_directory()

    async def to_absolute_path(self, filepath: str) -> str:
        return await self._shell.to_absolute_path(filepath)

    async def check_file_access(
        self,
        filepath: str,
        permissions: int,
    ) -> bool:
        return await self._shell.check_file_access(filepath, permissions)

    async def to_relative_path(
        self,
        base_path: str,
        absolute_path: str,
    ) -> str:
        return await self._shell.to_relative_path(base_path, absolute_path)

    async def change_directory(self, path: str) -> None:
        await self._shell.change_directory(path)

    async def assume_admin(
        self,
        password: Optional[str] = None,
        silent: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return await self._shell.assume_admin(password=password, silent=silent)

    async def run(
        self,
        command: str,
        command_input: Optional[str] = None,
        path: Optional[str] = None,
        env: Optional[Dict[str, str]] = None,
        as_shell: bool = False,
        silent: bool = False,
        timeout: Optional[float] = None,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return await self._shell.run(
            command,
            command_input=command_input,
            path=path,
            env=env,
            as_shell=as_shell,
            silent=silent,
            timeout=timeout,
            check=check,
        )

    async def copy(
        self,
        source_directory: str,
        destination_directory: str,
        recursive: bool = False,
        silent: bool = False,
    ) -> None:
        await self._shell.copy(
            source_directory,
            destination_directory,
            recursive=recursive,
            silent=silent,
        )

    async def move(
        self,
        source_directory: str,
        destination_directory: str,
        silent: bool = False,
    ) -> None:
        await self._shell.move(
            source_directory,
            destination_directory,
            silent=silent,
        )

    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return await self._shell.eval(
            command,
            env=env,
            silent=silent,
        )

    async def touch(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
        silent: bool = False,
    ) -> None:
        await self._shell.touch(
            filepath,
            is_bytes=is_bytes,
            overwrite=overwrite,
        )

    async def append_to_envfile(
        self,
        variable_name: str,
        variable_value: str,
        silent: bool = False,
    ) -> None:
        await self._shell.append_to_envfile(
            variable_name,
            variable_value,
        )

    async def check_path_exists(
        self,
        filepath: str,
        silent: bool = False,
    ) -> bool:
        return await self._shell.check_path_exists(filepath)

    async def create_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
        silent: bool = False,
    ) -> Optional[Union[TextIO, BinaryIO]]:
        return await self._shell.create_file(
            filepath,
            is_bytes=is_bytes,
            overwrite=overwrite,
        )

    async def open_or_create_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        overwrite: bool = False,
        silent: bool = False,
    ) -> Union[TextIO, BinaryIO]:
        return await self._shell.open_or_create_file(
            filepath,
            is_bytes=is_bytes,
            overwrite=overwrite,
        )

    async def open_existing_file(
        self,
        filepath: str,
        is_bytes: bool = False,
        write_mode: str = 'a+',
        silent: bool = False,
    ) -> Union[TextIO, BinaryIO]:
        return await self._shell.open_existing_file(
            filepath,
            is_bytes=is_bytes,
            write_mode=write_mode,
        )

    async def pipe_to_file(
        self,
        filepath: str,
        data: Union[str, bytes],
        overwrite: bool = False,
        silent: bool = False,
    ) -> None:
        await self._shell.pipe_to_file(
            filepath,
            data,
            overwrite=overwrite,
        )

    async def read_file(
        self,
        filepath: str,
        silent: bool = False,
    ) -> str:
        return await self._shell.read_file(
            filepath,
            is_bytes=False,
        )

    async def read_file_as_bytes(
        self,
        filepath: str,
        silent: bool = False,
    ) -> bytes:
        return await self._shell.read_file(
            filepath,
            is_bytes=True,
        )

    async def create_directory(self, path: str) -> None:
        await self._shell.create_directory(path)

    async def source(
        self,
        filepath: Optional[str] = None,
        silent: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return await self._shell.source(
            filepath=filepath,
            silent=silent,
        )

    async def rm(
        self,
        path: str,
        pattern: Optional[str] = None,
        recurse: bool = False,
        silent: bool = False,
    ) -> None:
        await self._shell.rm(
            path,
            pattern=pattern,
            recurse=recurse,
        )

    async def close(self) -> None:
        await self._shell.close()

    def abort(self) -> None:
        self._shell.abort()
