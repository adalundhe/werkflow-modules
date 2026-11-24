import platform
from typing import Dict, Optional, Type
from werkflow_core import Module
from .architecture.types import ArchitectureType
from .configuration import Configuration
from .exceptions import (
    UnsupportedArchitectureException,
    UnsupportedOperatingSystemException
)
from .operating_system import (
    Linux,
    MacOS,
    Windows,
    OperatingSystem,
    OperatingSystemType
)
from .users import Users


class System(Module):
    dependencies = ['psutil', 'distro']

    def __init__(self) -> None:
        super().__init__()

        self._supported_operating_systems: Dict[OperatingSystemType, Type[OperatingSystem]] = {
            OperatingSystemType.LINUX: Linux,
            OperatingSystemType.MAC_OS: MacOS,
            OperatingSystemType.WINDOWS: Windows
        }

        self._supported_architectures: Dict[str, ArchitectureType] = {
            architecture.value.lower(): architecture for architecture in ArchitectureType
        }

        self.users = Users()

        operating_system_type = OperatingSystem.detect()
        if operating_system_type is None or operating_system_type not in self._supported_operating_systems:
            raise UnsupportedOperatingSystemException(
                [os_option.value for os_option in self._supported_operating_systems.keys()]
            )

        self.os: OperatingSystem = self._supported_operating_systems[operating_system_type]()

        raw_machine = platform.machine()
        processor_architecture: Optional[ArchitectureType] = self._supported_architectures.get(
            raw_machine.lower()
        )

        self.architecture = (
            self.os.supported_architectures.get(processor_architecture)
            if processor_architecture is not None
            else None
        )

        if self.architecture is None:
            raise UnsupportedArchitectureException(
                self.os.name,
                raw_machine,
                list(self.os.supported_architectures.values()),
            )

        self.configuration = Configuration()
