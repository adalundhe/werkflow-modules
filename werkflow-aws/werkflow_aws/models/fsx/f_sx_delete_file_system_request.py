from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_delete_file_system_lustre_configuration import FSxDeleteFileSystemLustreConfiguration
from .f_sx_delete_file_system_open_zfs_configuration import FSxDeleteFileSystemOpenZFSConfiguration
from .f_sx_delete_file_system_windows_configuration import FSxDeleteFileSystemWindowsConfiguration


class FSxDeleteFileSystemRequest(BaseModel):
    FileSystemId: StrictStr
    ClientRequestToken: StrictStr | None = None
    WindowsConfiguration: FSxDeleteFileSystemWindowsConfiguration | None = None
    LustreConfiguration: FSxDeleteFileSystemLustreConfiguration | None = None
    OpenZFSConfiguration: FSxDeleteFileSystemOpenZFSConfiguration | None = None
