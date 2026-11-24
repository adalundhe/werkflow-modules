import os
import shutil
from typing import Dict, List, Optional, Type

from werkflow_system import Linux, LinuxDistroFamily, OperatingSystemType, System

from .base_shell import BaseShell
from .bash_shell import BashShell
from .cmd_shell import CmdShell
from .fish_shell import FishShell
from .powershell_shell import PowerShellShell
from .sh_shell import ShShell
from .shell_type import ShellType
from .zsh_shell import ZSHShell


_SHELL_TYPE_MAP: Dict[ShellType, Type[BaseShell]] = {
    ShellType.ZSH: ZSHShell,
    ShellType.BASH: BashShell,
    ShellType.SH: ShShell,
    ShellType.ASH: ShShell,
    ShellType.DASH: ShShell,
    ShellType.FISH: FishShell,
    ShellType.POWERSHELL: PowerShellShell,
    ShellType.PWSH: PowerShellShell,
    ShellType.CMD: CmdShell,
}

_SHELL_NAME_TO_CLASS: Dict[str, Type[BaseShell]] = {
    'zsh': ZSHShell,
    'bash': BashShell,
    'sh': ShShell,
    'ash': ShShell,
    'dash': ShShell,
    'fish': FishShell,
    'pwsh': PowerShellShell,
    'pwsh.exe': PowerShellShell,
    'powershell': PowerShellShell,
    'powershell.exe': PowerShellShell,
    'cmd': CmdShell,
    'cmd.exe': CmdShell,
}

_DISTRO_ID_SHELL_PREFERENCES: Dict[str, List[Type[BaseShell]]] = {
    'kali': [ZSHShell, BashShell, ShShell],
    'manjaro': [ZSHShell, BashShell, ShShell],
    'cachyos': [FishShell, BashShell, ZSHShell, ShShell],
    'alpine': [BashShell, ShShell],
    'postmarketos': [BashShell, ShShell],
}

_DISTRO_FAMILY_SHELL_PREFERENCES: Dict[LinuxDistroFamily, List[Type[BaseShell]]] = {
    LinuxDistroFamily.DEBIAN: [BashShell, ZSHShell, ShShell],
    LinuxDistroFamily.REDHAT: [BashShell, ZSHShell, ShShell],
    LinuxDistroFamily.AMAZON: [BashShell, ShShell],
    LinuxDistroFamily.ARCH: [BashShell, ZSHShell, FishShell, ShShell],
    LinuxDistroFamily.ALPINE: [BashShell, ShShell],
    LinuxDistroFamily.SUSE: [BashShell, ZSHShell, ShShell],
    LinuxDistroFamily.GENTOO: [BashShell, ZSHShell, ShShell],
    LinuxDistroFamily.VOID: [BashShell, ShShell],
    LinuxDistroFamily.NIXOS: [BashShell, ZSHShell, ShShell],
    LinuxDistroFamily.SLACKWARE: [BashShell, ShShell],
    LinuxDistroFamily.GENERIC: [BashShell, ZSHShell, ShShell],
}

_SHELL_BINARY_CANDIDATES: Dict[Type[BaseShell], List[str]] = {
    ZSHShell: ['zsh'],
    BashShell: ['bash'],
    FishShell: ['fish'],
    ShShell: ['ash', 'dash', 'sh'],
    PowerShellShell: ['pwsh', 'pwsh.exe', 'powershell.exe', 'powershell'],
    CmdShell: ['cmd.exe', 'cmd'],
}


class ShellResolver:

    @classmethod
    def _is_available(cls, shell_cls: Type[BaseShell]) -> bool:
        for candidate in _SHELL_BINARY_CANDIDATES.get(shell_cls, []):
            if shutil.which(candidate) is not None:
                return True
        return False

    @classmethod
    def _detect_from_env(cls) -> Optional[Type[BaseShell]]:
        env_shell = os.environ.get('SHELL', '').strip()
        if not env_shell:
            return None

        basename = os.path.basename(env_shell).lower()
        shell_cls = _SHELL_NAME_TO_CLASS.get(basename)
        if shell_cls is not None and (os.path.exists(env_shell) or cls._is_available(shell_cls)):
            return shell_cls
        return None

    @classmethod
    def resolve(
        cls,
        system: System,
        shell_type: Optional[ShellType] = None,
    ) -> Type[BaseShell]:
        if shell_type is not None:
            return _SHELL_TYPE_MAP[shell_type]

        os_type = system.os.type

        if os_type == OperatingSystemType.WINDOWS:
            win_candidates: List[Type[BaseShell]] = [PowerShellShell, CmdShell]
            for candidate in win_candidates:
                if cls._is_available(candidate):
                    return candidate
            return PowerShellShell

        if os_type == OperatingSystemType.MAC_OS:
            env_cls = cls._detect_from_env()
            if env_cls is not None:
                return env_cls
            mac_candidates: List[Type[BaseShell]] = [ZSHShell, BashShell, ShShell]
            for candidate in mac_candidates:
                if cls._is_available(candidate):
                    return candidate
            return ZSHShell

        if os_type == OperatingSystemType.LINUX:
            env_cls = cls._detect_from_env()
            if env_cls is not None:
                return env_cls

            preferences: List[Type[BaseShell]] = [BashShell, ZSHShell, ShShell]
            if isinstance(system.os, Linux):
                if system.os.id in _DISTRO_ID_SHELL_PREFERENCES:
                    preferences = _DISTRO_ID_SHELL_PREFERENCES[system.os.id]
                else:
                    preferences = _DISTRO_FAMILY_SHELL_PREFERENCES.get(
                        system.os.family,
                        preferences,
                    )

            for candidate in preferences:
                if cls._is_available(candidate):
                    return candidate
            return ShShell

        return ShShell
