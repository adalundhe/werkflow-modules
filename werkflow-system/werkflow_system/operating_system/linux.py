import platform
import shutil
from typing import Dict, List, Optional

try:
    import distro
except ImportError:
    distro = None  # type: ignore[assignment]

from werkflow_system.architecture.types import ArchitectureType

from .base import OperatingSystem
from .types import LinuxDistroFamily, OperatingSystemType


_DISTRO_FAMILY_MAP: Dict[str, LinuxDistroFamily] = {
    'debian': LinuxDistroFamily.DEBIAN,
    'ubuntu': LinuxDistroFamily.DEBIAN,
    'linuxmint': LinuxDistroFamily.DEBIAN,
    'mint': LinuxDistroFamily.DEBIAN,
    'pop': LinuxDistroFamily.DEBIAN,
    'kali': LinuxDistroFamily.DEBIAN,
    'raspbian': LinuxDistroFamily.DEBIAN,
    'elementary': LinuxDistroFamily.DEBIAN,
    'zorin': LinuxDistroFamily.DEBIAN,
    'mx': LinuxDistroFamily.DEBIAN,
    'devuan': LinuxDistroFamily.DEBIAN,
    'parrot': LinuxDistroFamily.DEBIAN,
    'deepin': LinuxDistroFamily.DEBIAN,
    'rhel': LinuxDistroFamily.REDHAT,
    'fedora': LinuxDistroFamily.REDHAT,
    'centos': LinuxDistroFamily.REDHAT,
    'rocky': LinuxDistroFamily.REDHAT,
    'almalinux': LinuxDistroFamily.REDHAT,
    'alma': LinuxDistroFamily.REDHAT,
    'ol': LinuxDistroFamily.REDHAT,
    'oracle': LinuxDistroFamily.REDHAT,
    'nobara': LinuxDistroFamily.REDHAT,
    'scientific': LinuxDistroFamily.REDHAT,
    'eurolinux': LinuxDistroFamily.REDHAT,
    'amzn': LinuxDistroFamily.AMAZON,
    'amazon': LinuxDistroFamily.AMAZON,
    'arch': LinuxDistroFamily.ARCH,
    'manjaro': LinuxDistroFamily.ARCH,
    'endeavouros': LinuxDistroFamily.ARCH,
    'garuda': LinuxDistroFamily.ARCH,
    'cachyos': LinuxDistroFamily.ARCH,
    'steamos': LinuxDistroFamily.ARCH,
    'artix': LinuxDistroFamily.ARCH,
    'arcolinux': LinuxDistroFamily.ARCH,
    'alpine': LinuxDistroFamily.ALPINE,
    'postmarketos': LinuxDistroFamily.ALPINE,
    'opensuse': LinuxDistroFamily.SUSE,
    'opensuse-leap': LinuxDistroFamily.SUSE,
    'opensuse-tumbleweed': LinuxDistroFamily.SUSE,
    'sles': LinuxDistroFamily.SUSE,
    'sled': LinuxDistroFamily.SUSE,
    'suse': LinuxDistroFamily.SUSE,
    'gentoo': LinuxDistroFamily.GENTOO,
    'funtoo': LinuxDistroFamily.GENTOO,
    'calculate': LinuxDistroFamily.GENTOO,
    'void': LinuxDistroFamily.VOID,
    'nixos': LinuxDistroFamily.NIXOS,
    'slackware': LinuxDistroFamily.SLACKWARE,
}

_FAMILY_PACKAGE_MANAGERS: Dict[LinuxDistroFamily, List[str]] = {
    LinuxDistroFamily.DEBIAN: ['apt', 'apt-get', 'dpkg'],
    LinuxDistroFamily.REDHAT: ['dnf', 'yum', 'microdnf', 'rpm'],
    LinuxDistroFamily.AMAZON: ['dnf', 'yum', 'rpm'],
    LinuxDistroFamily.ARCH: ['pacman'],
    LinuxDistroFamily.ALPINE: ['apk'],
    LinuxDistroFamily.SUSE: ['zypper'],
    LinuxDistroFamily.GENTOO: ['emerge'],
    LinuxDistroFamily.VOID: ['xbps-install'],
    LinuxDistroFamily.NIXOS: ['nix', 'nix-env'],
    LinuxDistroFamily.SLACKWARE: ['slackpkg'],
    LinuxDistroFamily.GENERIC: ['apt', 'dnf', 'yum', 'pacman', 'apk', 'zypper', 'emerge', 'xbps-install', 'nix'],
}


class Linux(OperatingSystem):

    def __init__(self) -> None:
        super().__init__()

        raw_id = ''
        raw_like = ''
        raw_name = ''
        raw_version = ''
        raw_codename = ''

        if distro is not None:
            raw_id = (distro.id() or '').strip().lower()
            raw_like = (distro.like() or '').strip().lower()
            raw_name = (distro.name() or '').strip()
            raw_version = (distro.version() or '').strip()
            raw_codename = (distro.codename() or '').strip()

        self.id: str = raw_id
        self.like: List[str] = [token for token in raw_like.split() if token]
        self.codename: str = raw_codename
        self.kernel_version: str = platform.release()
        self.name: str = raw_name or (raw_id.capitalize() if raw_id else 'Linux')
        self.version: str = raw_version or self.kernel_version
        self.type = OperatingSystemType.LINUX
        self.family: LinuxDistroFamily = self._detect_family(self.id, self.like)
        self.package_manager: Optional[str] = self._detect_package_manager(self.family)

        self.supported_architectures = {
            ArchitectureType.ARM_64: 'arm64',
            ArchitectureType.x86_64: 'x86_64',
            ArchitectureType.AMD_64: 'AMD64',
            ArchitectureType.AARCH64: 'aarch64',
            ArchitectureType.I386: 'i386',
            ArchitectureType.I686: 'i686',
            ArchitectureType.X86: 'x86',
            ArchitectureType.ARMV7L: 'armv7l',
            ArchitectureType.ARMV6L: 'armv6l',
            ArchitectureType.PPC64LE: 'ppc64le',
            ArchitectureType.S390X: 's390x',
            ArchitectureType.RISCV64: 'riscv64',
        }

    @classmethod
    def _detect_family(
        cls,
        distro_id: str,
        distro_like: List[str],
    ) -> LinuxDistroFamily:
        if distro_id in _DISTRO_FAMILY_MAP:
            return _DISTRO_FAMILY_MAP[distro_id]

        for parent in distro_like:
            if parent in _DISTRO_FAMILY_MAP:
                return _DISTRO_FAMILY_MAP[parent]

        return LinuxDistroFamily.GENERIC

    @classmethod
    def _detect_package_manager(
        cls,
        family: LinuxDistroFamily,
    ) -> Optional[str]:
        candidates = _FAMILY_PACKAGE_MANAGERS.get(
            family,
            _FAMILY_PACKAGE_MANAGERS[LinuxDistroFamily.GENERIC],
        )
        for candidate in candidates:
            if shutil.which(candidate) is not None:
                return candidate
        return candidates[0] if family != LinuxDistroFamily.GENERIC and candidates else None
