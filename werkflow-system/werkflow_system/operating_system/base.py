import platform
from typing import Dict, Optional
import psutil
from werkflow_system.architecture.types import ArchitectureType
from .types import OperatingSystemType


class OperatingSystem:

    def __init__(self) -> None:
        self.name: str = ''
        self.type: Optional[OperatingSystemType] = None
        self.version: str = platform.release()
        self.supported_architectures: Dict[ArchitectureType, str] = {}

    @classmethod
    def detect(cls) -> Optional[OperatingSystemType]:
        if psutil.MACOS:
            return OperatingSystemType.MAC_OS

        if psutil.WINDOWS:
            return OperatingSystemType.WINDOWS

        if psutil.LINUX:
            return OperatingSystemType.LINUX

        system_name = platform.system()
        if system_name == OperatingSystemType.MAC_OS.value:
            return OperatingSystemType.MAC_OS
        if system_name == OperatingSystemType.WINDOWS.value:
            return OperatingSystemType.WINDOWS
        if system_name == OperatingSystemType.LINUX.value:
            return OperatingSystemType.LINUX

        return None
