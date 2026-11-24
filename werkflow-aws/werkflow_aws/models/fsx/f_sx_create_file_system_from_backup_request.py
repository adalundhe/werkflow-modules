from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_create_file_system_lustre_configuration import FSxCreateFileSystemLustreConfiguration
from .f_sx_create_file_system_open_zfs_configuration import FSxCreateFileSystemOpenZFSConfiguration
from .f_sx_create_file_system_windows_configuration import FSxCreateFileSystemWindowsConfiguration
from .f_sx_tag import FSxTag


class FSxCreateFileSystemFromBackupRequest(BaseModel):
    BackupId: StrictStr
    SubnetIds: list[StrictStr]
    ClientRequestToken: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[FSxTag] | None = None
    WindowsConfiguration: FSxCreateFileSystemWindowsConfiguration | None = None
    LustreConfiguration: FSxCreateFileSystemLustreConfiguration | None = None
    StorageType: Literal['SSD', 'HDD', 'INTELLIGENT_TIERING'] | None = None
    KmsKeyId: StrictStr | None = None
    FileSystemTypeVersion: StrictStr | None = None
    OpenZFSConfiguration: FSxCreateFileSystemOpenZFSConfiguration | None = None
    StorageCapacity: StrictInt | None = None
    NetworkType: Literal['IPV4', 'DUAL'] | None = None
