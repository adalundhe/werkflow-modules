from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_create_file_system_lustre_configuration import FSxCreateFileSystemLustreConfiguration
from .f_sx_create_file_system_ontap_configuration import FSxCreateFileSystemOntapConfiguration
from .f_sx_create_file_system_open_zfs_configuration import FSxCreateFileSystemOpenZFSConfiguration
from .f_sx_create_file_system_windows_configuration import FSxCreateFileSystemWindowsConfiguration
from .f_sx_tag import FSxTag


class FSxCreateFileSystemRequest(BaseModel):
    FileSystemType: Literal['WINDOWS', 'LUSTRE', 'ONTAP', 'OPENZFS']
    SubnetIds: list[StrictStr]
    ClientRequestToken: StrictStr | None = None
    StorageCapacity: StrictInt | None = None
    StorageType: Literal['SSD', 'HDD', 'INTELLIGENT_TIERING'] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[FSxTag] | None = None
    KmsKeyId: StrictStr | None = None
    WindowsConfiguration: FSxCreateFileSystemWindowsConfiguration | None = None
    LustreConfiguration: FSxCreateFileSystemLustreConfiguration | None = None
    OntapConfiguration: FSxCreateFileSystemOntapConfiguration | None = None
    FileSystemTypeVersion: StrictStr | None = None
    OpenZFSConfiguration: FSxCreateFileSystemOpenZFSConfiguration | None = None
    NetworkType: Literal['IPV4', 'DUAL'] | None = None
