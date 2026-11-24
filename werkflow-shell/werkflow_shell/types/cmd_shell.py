import ctypes
import os
import shlex
import shutil
import subprocess
from typing import Dict, List, Optional

from .base_shell import BaseShell
from .shell_type import ShellType


_CMD_ENV_SENTINEL = '__WERKFLOW_CMD_ENV_START__'


class CmdShell(BaseShell):
    shell_type: ShellType = ShellType.CMD

    def _detect_executable(self) -> str:
        return (
            os.environ.get('COMSPEC')
            or shutil.which('cmd.exe')
            or shutil.which('cmd')
            or 'cmd.exe'
        )

    def _default_envfile_name(self) -> str:
        return 'werkflow_env.cmd'

    def _build_shell_command(self, command: str) -> List[str]:
        return [self.shell_executable, '/d', '/s', '/c', command]

    def _split_command(self, command: str) -> List[str]:
        tokens = shlex.split(command, posix=False)
        cleaned: List[str] = []
        for token in tokens:
            if len(token) >= 2 and token[0] == token[-1] and token[0] in ('"', "'"):
                cleaned.append(token[1:-1])
            else:
                cleaned.append(token)
        return cleaned

    def _format_envfile_entry(
        self,
        variable_name: str,
        variable_value: str,
    ) -> str:
        escaped_value = variable_value.replace('"', '""')
        return f'set "{variable_name}={escaped_value}"'

    @staticmethod
    def _parse_captured_env(stdout: Optional[str]) -> Dict[str, str]:
        if not stdout or _CMD_ENV_SENTINEL not in stdout:
            return {}
        _, _, env_block = stdout.partition(_CMD_ENV_SENTINEL)
        parsed: Dict[str, str] = {}
        for line in env_block.splitlines():
            line = line.strip()
            if '=' in line:
                key, _, value = line.partition('=')
                if key:
                    parsed[key] = value
        return parsed

    @staticmethod
    def _is_windows_admin() -> bool:
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())  # type: ignore[attr-defined]
        except Exception:
            return False

    async def assume_admin(
        self,
        password: Optional[str] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        if self._is_windows_admin():
            return subprocess.CompletedProcess(
                args=[self.shell_executable],
                returncode=0,
                stdout='Administrator\n',
                stderr='',
            )
        return await self.run('net session', as_shell=True, silent=silent)

    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        wrapped = f'{command} && echo {_CMD_ENV_SENTINEL} && set'
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
        escaped_path = absolute_path.replace('"', '""')
        wrapped = f'call "{escaped_path}" && echo {_CMD_ENV_SENTINEL} && set'
        result = await self.run(
            wrapped,
            as_shell=True,
            silent=True,
        )
        if result.returncode == 0:
            captured = self._parse_captured_env(result.stdout)
            self._update_env_from_mapping(captured)
        return result
