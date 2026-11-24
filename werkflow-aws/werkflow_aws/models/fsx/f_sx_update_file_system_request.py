from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_update_file_system_lustre_configuration import FSxUpdateFileSystemLustreConfiguration
from .f_sx_update_file_system_ontap_configuration import FSxUpdateFileSystemOntapConfiguration
from .f_sx_update_file_system_open_zfs_configuration import FSxUpdateFileSystemOpenZFSConfiguration
from .f_sx_update_file_system_windows_configuration import FSxUpdateFileSystemWindowsConfiguration


class FSxUpdateFileSystemRequest(BaseModel):
    FileSystemId: StrictStr
    ClientRequestToken: StrictStr | None = None
    StorageCapacity: StrictInt | None = None
    WindowsConfiguration: FSxUpdateFileSystemWindowsConfiguration | None = None
    LustreConfiguration: FSxUpdateFileSystemLustreConfiguration | None = None
    OntapConfiguration: FSxUpdateFileSystemOntapConfiguration | None = None
    OpenZFSConfiguration: FSxUpdateFileSystemOpenZFSConfiguration | None = None
    StorageType: Literal['SSD', 'HDD', 'INTELLIGENT_TIERING'] | None = None
    FileSystemTypeVersion: StrictStr | None = None
    NetworkType: Literal['IPV4', 'DUAL'] | None = None
