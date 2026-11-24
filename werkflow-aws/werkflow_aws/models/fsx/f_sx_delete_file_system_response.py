from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_delete_file_system_lustre_response import FSxDeleteFileSystemLustreResponse
from .f_sx_delete_file_system_open_zfs_response import FSxDeleteFileSystemOpenZFSResponse
from .f_sx_delete_file_system_windows_response import FSxDeleteFileSystemWindowsResponse


class FSxDeleteFileSystemResponse(BaseModel):
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    WindowsResponse: FSxDeleteFileSystemWindowsResponse | None = None
    LustreResponse: FSxDeleteFileSystemLustreResponse | None = None
    OpenZFSResponse: FSxDeleteFileSystemOpenZFSResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
