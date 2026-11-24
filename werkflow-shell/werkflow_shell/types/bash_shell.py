import os
import shutil
from typing import Optional

from werkflow_system import OperatingSystemType, System

from .posix_shell import POSIXShell
from .shell_type import ShellType


class BashShell(POSIXShell):
    shell_type: ShellType = ShellType.BASH
    _source_command: str = 'source'

    def __init__(self, system: Optional[System] = None) -> None:
        super().__init__(system=system)

    def _detect_executable(self) -> str:
        return (
            shutil.which('bash')
            or ('/bin/bash' if shutil.which('/bin/bash') else None)
            or ('/usr/bin/bash' if shutil.which('/usr/bin/bash') else None)
            or '/bin/bash'
        )

    def _default_envfile_name(self) -> str:
        if self._system.os.type == OperatingSystemType.MAC_OS:
            bashrc = os.path.join(self._home, '.bashrc')
            if not os.path.exists(bashrc):
                return '.bash_profile'
        return '.bashrc'
