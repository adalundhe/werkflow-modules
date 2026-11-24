from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_ontap_unix_file_system_user import FSxOntapUnixFileSystemUser
from .f_sx_ontap_windows_file_system_user import FSxOntapWindowsFileSystemUser


class FSxOntapFileSystemIdentity(BaseModel):
    Type: StrictStr | None = None
    UnixUser: FSxOntapUnixFileSystemUser | None = None
    WindowsUser: FSxOntapWindowsFileSystemUser | None = None
