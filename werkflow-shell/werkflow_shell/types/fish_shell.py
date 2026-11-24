import os
import shlex
import shutil
import subprocess
from typing import Dict, List, Optional

from .posix_shell import POSIXShell, _ENV_SENTINEL
from .shell_type import ShellType


class FishShell(POSIXShell):
    shell_type: ShellType = ShellType.FISH
    _source_command: str = 'source'

    def _detect_executable(self) -> str:
        return (
            shutil.which('fish')
            or ('/usr/bin/fish' if shutil.which('/usr/bin/fish') else None)
            or ('/opt/homebrew/bin/fish' if shutil.which('/opt/homebrew/bin/fish') else None)
            or '/usr/bin/fish'
        )

    def _default_envfile_name(self) -> str:
        return 'config.fish'

    def _default_envfile_path(self) -> str:
        return os.path.join(self._home, '.config', 'fish', self.envfile_name)

    def _build_shell_command(self, command: str) -> List[str]:
        return [self.shell_executable, '-c', command]

    def _format_envfile_entry(
        self,
        variable_name: str,
        variable_value: str,
    ) -> str:
        return f'set -gx {variable_name} {shlex.quote(variable_value)}'

    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        wrapped = (
            f'eval ({command}); and printf "\\n{_ENV_SENTINEL}\\n"; and env'
        )
        result = await self.run(
            wrapped,
            env=env,
            as_shell=True,
            silent=True,
        )
        if result.returncode == 0:
            captured = self._parse_captured_env(result.stdout)
            self._update_env_from_mapping(captured)
        return result

    async def source(
        self,
        filepath: Optional[str] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        target_path = filepath if filepath is not None else self.envfile_path
        absolute_path = await self.to_absolute_path(target_path)
        wrapped = (
            f'source {shlex.quote(absolute_path)}; '
            f'and printf "\\n{_ENV_SENTINEL}\\n"; and env'
        )
        result = await self.run(
            wrapped,
            as_shell=True,
            silent=True,
        )
        if result.returncode == 0:
            captured = self._parse_captured_env(result.stdout)
            self._update_env_from_mapping(captured)
        return result
