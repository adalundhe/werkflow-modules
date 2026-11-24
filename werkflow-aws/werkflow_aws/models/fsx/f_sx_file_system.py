from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_file_system_failure_details import FSxFileSystemFailureDetails
from .f_sx_lustre_file_system_configuration import FSxLustreFileSystemConfiguration
from .f_sx_ontap_file_system_configuration import FSxOntapFileSystemConfiguration
from .f_sx_open_zfs_file_system_configuration import FSxOpenZFSFileSystemConfiguration
from .f_sx_tag import FSxTag
from .f_sx_windows_file_system_configuration import FSxWindowsFileSystemConfiguration

if TYPE_CHECKING:
    from .f_sx_administrative_action import FSxAdministrativeAction


class FSxFileSystem(BaseModel):
    OwnerId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FileSystemId: StrictStr | None = None
    FileSystemType: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    FailureDetails: FSxFileSystemFailureDetails | None = None
    StorageCapacity: StrictInt | None = None
    StorageType: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    NetworkInterfaceIds: list[StrictStr] | None = None
    DNSName: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    WindowsConfiguration: FSxWindowsFileSystemConfiguration | None = None
    LustreConfiguration: FSxLustreFileSystemConfiguration | None = None
    AdministrativeActions: list[FSxAdministrativeAction] | None = None
    OntapConfiguration: FSxOntapFileSystemConfiguration | None = None
    FileSystemTypeVersion: StrictStr | None = None
    OpenZFSConfiguration: FSxOpenZFSFileSystemConfiguration | None = None
    NetworkType: StrictStr | None = None
