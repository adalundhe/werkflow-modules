import shutil

from .posix_shell import POSIXShell
from .shell_type import ShellType


class ZSHShell(POSIXShell):
    shell_type: ShellType = ShellType.ZSH
    _source_command: str = 'source'

    def _detect_executable(self) -> str:
        return (
            shutil.which('zsh')
            or ('/bin/zsh' if shutil.which('/bin/zsh') else None)
            or ('/usr/bin/zsh' if shutil.which('/usr/bin/zsh') else None)
            or '/bin/zsh'
        )

    def _default_envfile_name(self) -> str:
        return '.zshrc'
