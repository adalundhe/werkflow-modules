import os
import shlex
import shutil
import subprocess
from typing import Dict, List, Optional

from .base_shell import BaseShell
from .shell_type import ShellType


_ENV_SENTINEL = '__WERKFLOW_ENV_START__'


class POSIXShell(BaseShell):
    shell_type: ShellType = ShellType.SH
    _source_command: str = '.'

    def _detect_executable(self) -> str:
        return shutil.which('sh') or '/bin/sh'

    def _default_envfile_name(self) -> str:
        return '.profile'

    def _build_shell_command(self, command: str) -> List[str]:
        return [self.shell_executable, '-c', command]

    def _format_envfile_entry(
        self,
        variable_name: str,
        variable_value: str,
    ) -> str:
        return f'export {variable_name}={shlex.quote(variable_value)}'

    @staticmethod
    def _parse_captured_env(stdout: Optional[str]) -> Dict[str, str]:
        if not stdout or _ENV_SENTINEL not in stdout:
            return {}

        _, _, env_block = stdout.partition(f'{_ENV_SENTINEL}\n')
        parsed: Dict[str, str] = {}
        for line in env_block.splitlines():
            if '=' in line:
                key, _, value = line.partition('=')
                if key and key.replace('_', '').isalnum() and not key[0].isdigit():
                    parsed[key] = value
        return parsed

    async def assume_admin(
        self,
        password: Optional[str] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
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
            return await self.run(
                f'{shlex.quote(sudo_bin)} -n -v',
                silent=silent,
            )

        doas_bin = await self.which('doas')
        if doas_bin:
            cmd = f'{shlex.quote(doas_bin)} true'
            return await self.run(
                cmd,
                command_input=f'{password}\n' if password is not None else None,
                silent=silent,
            )

        su_bin = await self.which('su')
        if su_bin:
            return await self.run(
                f'{shlex.quote(su_bin)} -c true',
                command_input=f'{password}\n' if password is not None else None,
                silent=silent,
            )

        return subprocess.CompletedProcess(
            args=['sudo'],
            returncode=127,
            stdout='',
            stderr='No privilege escalation utility found (tried sudo, doas, su).',
        )

    async def eval(
        self,
        command: str,
        env: Optional[Dict[str, str]] = None,
        silent: Optional[bool] = None,
    ) -> subprocess.CompletedProcess[str]:
        wrapped = (
            f'eval "$({command})" && printf "\\n{_ENV_SENTINEL}\\n" && env'
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
            f'{self._source_command} {shlex.quote(absolute_path)} '
            f'&& printf "\\n{_ENV_SENTINEL}\\n" && env'
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
