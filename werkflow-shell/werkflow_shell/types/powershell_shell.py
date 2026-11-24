import ctypes
import json
import os
import shlex
import shutil
import subprocess
from typing import Dict, List, Optional

from werkflow_system import OperatingSystemType, System

from .base_shell import BaseShell
from .shell_type import ShellType


_PS_ENV_SENTINEL = '__WERKFLOW_PS_ENV_START__'


def _ps_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


class PowerShellShell(BaseShell):
    shell_type: ShellType = ShellType.POWERSHELL

    def __init__(self, system: Optional[System] = None) -> None:
        super().__init__(system=system)
        basename = os.path.basename(self.shell_executable).lower()
        if basename.startswith('pwsh'):
            self.shell_type = ShellType.PWSH
        else:
            self.shell_type = ShellType.POWERSHELL

    def _detect_executable(self) -> str:
        return (
            shutil.which('pwsh')
            or shutil.which('pwsh.exe')
            or shutil.which('powershell.exe')
            or shutil.which('powershell')
            or 'powershell.exe'
        )

    def _default_envfile_name(self) -> str:
        return 'Microsoft.PowerShell_profile.ps1'

    def _default_envfile_path(self) -> str:
        basename = os.path.basename(self.shell_executable).lower()
        is_pwsh = basename.startswith('pwsh')
        if self._system.os.type == OperatingSystemType.WINDOWS:
            folder = 'PowerShell' if is_pwsh else 'WindowsPowerShell'
            return os.path.join(self._home, 'Documents', folder, self.envfile_name)
        return os.path.join(self._home, '.config', 'powershell', self.envfile_name)

    def _build_shell_command(self, command: str) -> List[str]:
        return [
            self.shell_executable,
            '-NoProfile',
            '-NonInteractive',
            '-ExecutionPolicy',
            'Bypass',
            '-Command',
            command,
        ]

    def _split_command(self, command: str) -> List[str]:
        is_windows = self._system.os.type == OperatingSystemType.WINDOWS
        tokens = shlex.split(command, posix=not is_windows)
        if is_windows:
            cleaned: List[str] = []
            for token in tokens:
                if len(token) >= 2 and token[0] == token[-1] and token[0] in ('"', "'"):
                    cleaned.append(token[1:-1])
                else:
                    cleaned.append(token)
            return cleaned
        return tokens

    def _format_envfile_entry(
        self,
        variable_name: str,
        variable_value: str,
    ) -> str:
        return f'$env:{variable_name} = {_ps_quote(variable_value)}'

    @staticmethod
    def _parse_captured_env(stdout: Optional[str]) -> Dict[str, str]:
        if not stdout or _PS_ENV_SENTINEL not in stdout:
            return {}
        _, _, payload = stdout.partition(_PS_ENV_SENTINEL)
        payload = payload.strip()
        if not payload:
            return {}
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            return {}
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
        return {}

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
        if self._system.os.type == OperatingSystemType.WINDOWS:
            if self._is_windows_admin():
                return subprocess.CompletedProcess(
                    args=[self.shell_executable],
                    returncode=0,
                    stdout='True\n',
                    stderr='',
                )
            check_cmd = (
                '([Security.Principal.WindowsPrincipal] '
                '[Security.Principal.WindowsIdentity]::GetCurrent()'
                ').IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)'
            )
            result = await self.run(check_cmd, as_shell=True, silent=silent)
            if result.returncode == 0 and (result.stdout or '').strip().lower() == 'true':
                return result
            return subprocess.CompletedProcess(
                args=[self.shell_executable, '-Command', check_cmd],
                returncode=1,
                stdout=result.stdout or '',
                stderr=(
                    result.stderr
                    or 'Current PowerShell process is not elevated as Administrator.'
                ),
            )

        if hasattr(os, 'geteuid') and os.geteuid() == 0:
            return subprocess.CompletedProcess(
                args=['id', '-u'],
                returncode=0,
                stdout='0\n',
                stderr='',
            )

        sudo_bin = await self.which('sudo')
        if sudo_bin:
            if password is not None:
                return await self.run(
                    f'{shlex.quote(sudo_bin)} -S -v',
                    command_input=f'{password}\n',
                    silent=silent,
                )
            return await self.run(f'{shlex.quote(sudo_bin)} -n -v', silent=silent)

        return subprocess.CompletedProcess(
            args=['sudo'],
            returncode=127,
            stdout='',
            stderr='Privilege elevation requires Administrator or sudo.',
        )

    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        env_dump = (
            "$h = @{}; Get-ChildItem Env: | ForEach-Object { $h[$_.Name] = $_.Value }; "
            f"Write-Output '{_PS_ENV_SENTINEL}'; "
            "$h | ConvertTo-Json -Compress"
        )
        wrapped = f'Invoke-Expression ({command}); if ($?) {{ {env_dump} }}'
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
        env_dump = (
            "$h = @{}; Get-ChildItem Env: | ForEach-Object { $h[$_.Name] = $_.Value }; "
            f"Write-Output '{_PS_ENV_SENTINEL}'; "
            "$h | ConvertTo-Json -Compress"
        )
        wrapped = f'. {_ps_quote(absolute_path)}; if ($?) {{ {env_dump} }}'
        result = await self.run(
            wrapped,
            as_shell=True,
            silent=True,
        )
        if result.returncode == 0:
            captured = self._parse_captured_env(result.stdout)
            self._update_env_from_mapping(captured)
        return result
