import platform
from werkflow_system.architecture.types import ArchitectureType
from .base import OperatingSystem
from .types import OperatingSystemType


class Windows(OperatingSystem):

    def __init__(self) -> None:
        super().__init__()

        self.name = 'Windows'
        self.type = OperatingSystemType.WINDOWS
        self.version = self._detect_version()

        self.supported_architectures = {
            ArchitectureType.x86_64: 'x86_64',
            ArchitectureType.AMD_64: 'AMD64',
            ArchitectureType.ARM_64: 'arm64',
            ArchitectureType.AARCH64: 'aarch64',
            ArchitectureType.X86: 'x86',
            ArchitectureType.I386: 'i386',
            ArchitectureType.I686: 'i686',
        }

    @staticmethod
    def _detect_version() -> str:
        release = platform.release()
        version = platform.version()
        if release == '10' and version:
            parts = version.split('.')
            if len(parts) >= 3:
                try:
                    if int(parts[2]) >= 22000:
                        return '11'
                except ValueError:
                    pass
        return release or version
