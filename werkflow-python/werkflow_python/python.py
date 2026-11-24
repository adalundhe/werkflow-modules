import os
import pathlib
import platform
import shlex
import subprocess
import sys
from typing import List, Optional

from werkflow_core import Module
from werkflow_shell import Shell
from werkflow_system import OperatingSystemType


class Python(Module):
    dependencies = ['werkflow-shell', 'werkflow-system']

    def __init__(self) -> None:
        super().__init__()

        self.version: str = platform.python_version()
        self._shell = Shell()
        self._active_venv: Optional[str] = None

    def _is_windows(self) -> bool:
        return self._shell.os_type == OperatingSystemType.WINDOWS

    def _quote_arg(self, arg: str) -> str:
        if self._is_windows():
            escaped = arg.replace('"', '\\"')
            return f'"{escaped}"'
        return shlex.quote(arg)

    def _format_command(self, args: List[str]) -> str:
        return ' '.join(self._quote_arg(arg) for arg in args)

    def _venv_bin_dir(self, venv_root: str) -> str:
        subdir = 'Scripts' if self._is_windows() else 'bin'
        return os.path.join(venv_root, subdir)

    def _venv_activate_path(self, venv_root: str) -> str:
        return os.path.join(self._venv_bin_dir(venv_root), 'activate')

    def _venv_python_path(self, venv_root: str) -> str:
        executable = 'python.exe' if self._is_windows() else 'python'
        return os.path.join(self._venv_bin_dir(venv_root), executable)

    def _venv_pip_path(self, venv_root: str) -> str:
        executable = 'pip.exe' if self._is_windows() else 'pip'
        return os.path.join(self._venv_bin_dir(venv_root), executable)

    async def _resolve_venv_root(self, venv_path: str) -> str:
        absolute_path = await self._shell.to_absolute_path(venv_path)
        path_obj = pathlib.Path(absolute_path)

        lower_name = path_obj.name.lower()
        parent_lower = path_obj.parent.name.lower()

        if lower_name in (
            'activate',
            'activate.bat',
            'activate.ps1',
            'activate.csh',
            'activate.fish',
            'python',
            'python3',
            'python.exe',
            'pip',
            'pip3',
            'pip.exe',
        ) and parent_lower in ('bin', 'scripts'):
            return str(path_obj.parent.parent)

        if lower_name in ('bin', 'scripts') and (
            (path_obj.parent / 'pyvenv.cfg').exists()
            or (path_obj / 'activate').exists()
            or (path_obj / 'activate.bat').exists()
            or (path_obj / 'Activate.ps1').exists()
        ):
            return str(path_obj.parent)

        return str(path_obj)

    async def _detect_python_executable(self) -> str:
        if sys.executable:
            return sys.executable

        candidates = ('python', 'python3') if self._is_windows() else ('python3', 'python')
        for candidate in candidates:
            resolved = await self._shell.which(candidate)
            if resolved:
                return resolved

        return 'python' if self._is_windows() else 'python3'

    async def _resolve_pip_prefix(
        self,
        virtual_environment: Optional[str] = None,
    ) -> List[str]:
        if virtual_environment is not None:
            venv_root = await self._resolve_venv_root(virtual_environment)
            venv_python = self._venv_python_path(venv_root)
            venv_pip = self._venv_pip_path(venv_root)
            if os.path.exists(venv_python) or not os.path.exists(venv_pip):
                return [venv_python, '-m', 'pip']
            return [venv_pip]

        if self._active_venv is not None:
            venv_python = self._venv_python_path(self._active_venv)
            venv_pip = self._venv_pip_path(self._active_venv)
            if os.path.exists(venv_python) or not os.path.exists(venv_pip):
                return [venv_python, '-m', 'pip']
            return [venv_pip]

        python_executable = await self._detect_python_executable()
        return [python_executable, '-m', 'pip']

    async def set_python_version(
        self,
        version: Optional[str] = None,
        skip_if_exists: bool = True,
        force_reinstall: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        target_version = version if version is not None else self.version

        install_args = ['pyenv', 'install']
        if force_reinstall:
            install_args.append('-f')
        elif skip_if_exists:
            install_args.append('-s')
        install_args.append(target_version)

        install_result = await self._shell.run(
            self._format_command(install_args),
            silent=True,
        )
        if install_result.returncode != 0:
            raise RuntimeError(
                f"Failed to install Python version '{target_version}' with pyenv: "
                f"{install_result.stderr or install_result.stdout}"
            )

        global_result = await self._shell.run(
            self._format_command(['pyenv', 'global', target_version]),
            silent=True,
        )
        if global_result.returncode != 0:
            raise RuntimeError(
                f"Failed to set global Python version to '{target_version}' with pyenv: "
                f"{global_result.stderr or global_result.stdout}"
            )

        if not self._is_windows():
            eval_result = await self._shell.eval('pyenv init -', silent=True)
            if eval_result.returncode != 0:
                raise RuntimeError(
                    f"Failed to evaluate pyenv shell initialization: "
                    f"{eval_result.stderr or eval_result.stdout}"
                )

        self.version = target_version
        return global_result

    async def create_venv(
        self,
        environment_name: str,
    ) -> str:
        absolute_path = await self._shell.to_absolute_path(environment_name)
        python_executable = await self._detect_python_executable()

        result = await self._shell.run(
            self._format_command([python_executable, '-m', 'venv', absolute_path]),
            as_shell=False,
            silent=True,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to create virtual environment at '{absolute_path}': "
                f"{result.stderr or result.stdout}"
            )

        return self._venv_activate_path(absolute_path)

    async def install_requirements(
        self,
        requirements: List[str],
        virtual_environment: Optional[str] = None,
    ) -> subprocess.CompletedProcess[str]:
        if not requirements:
            return subprocess.CompletedProcess(
                args=[],
                returncode=0,
                stdout='',
                stderr='',
            )

        pip_prefix = await self._resolve_pip_prefix(virtual_environment)
        command = self._format_command([*pip_prefix, 'install', *requirements])

        return await self._shell.run(
            command,
            as_shell=False,
            silent=True,
        )

    async def install_requirements_from_file(
        self,
        install_requirements: Optional[List[str]] = None,
        filepath: str = 'requirements.txt',
        virtual_environment: Optional[str] = None,
    ) -> subprocess.CompletedProcess[str]:
        absolute_filepath = await self._shell.to_absolute_path(filepath)

        if install_requirements and len(install_requirements) > 0:
            requirements_content = '\n'.join(install_requirements) + '\n'
            await self._shell.pipe_to_file(
                absolute_filepath,
                requirements_content,
                overwrite=True,
                silent=True,
            )
        else:
            await self._shell.touch(
                absolute_filepath,
                silent=True,
            )

        pip_prefix = await self._resolve_pip_prefix(virtual_environment)
        command = self._format_command([*pip_prefix, 'install', '-r', absolute_filepath])

        return await self._shell.run(
            command,
            as_shell=False,
            silent=True,
        )

    async def activate_virtual_environment(
        self,
        virtual_environment_path: Optional[str] = None,
        *,
        virtual_envrionment_path: Optional[str] = None,
    ) -> str:
        target_path = (
            virtual_environment_path
            if virtual_environment_path is not None
            else virtual_envrionment_path
        )
        if target_path is None:
            raise ValueError("'virtual_environment_path' must be provided.")

        venv_root = await self._resolve_venv_root(target_path)
        venv_bin_dir = self._venv_bin_dir(venv_root)
        activate_location = self._venv_activate_path(venv_root)

        current_path = self._shell.env.get('PATH') or os.environ.get('PATH', '')
        path_entries = (
            [entry for entry in current_path.split(os.pathsep) if entry]
            if current_path
            else []
        )
        filtered_entries = [entry for entry in path_entries if entry != venv_bin_dir]
        self._shell.env['PATH'] = os.pathsep.join([venv_bin_dir, *filtered_entries])
        self._shell.env['VIRTUAL_ENV'] = venv_root
        self._shell.env.pop('PYTHONHOME', None)
        self._active_venv = venv_root

        return activate_location

    async def close(self) -> None:
        await self._shell.close()

    def abort(self) -> None:
        self._shell.abort()
