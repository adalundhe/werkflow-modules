import os
import shutil
from typing import Optional

from werkflow_system import Linux, LinuxDistroFamily, System

from .posix_shell import POSIXShell
from .shell_type import ShellType


class ShShell(POSIXShell):
    shell_type: ShellType = ShellType.SH
    _source_command: str = '.'

    def __init__(self, system: Optional[System] = None) -> None:
        super().__init__(system=system)
        basename = os.path.basename(self.shell_executable).lower()
        if basename == 'ash':
            self.shell_type = ShellType.ASH
        elif basename == 'dash':
            self.shell_type = ShellType.DASH
        else:
            self.shell_type = ShellType.SH

    def _detect_executable(self) -> str:
        if isinstance(self._system.os, Linux):
            if self._system.os.family == LinuxDistroFamily.ALPINE:
                return shutil.which('ash') or shutil.which('sh') or '/bin/sh'
            if self._system.os.family == LinuxDistroFamily.DEBIAN:
                return shutil.which('dash') or shutil.which('sh') or '/bin/sh'

        return shutil.which('sh') or '/bin/sh'

    def _default_envfile_name(self) -> str:
        return '.profile'
