from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_open_zfs_posix_file_system_user import FSxOpenZFSPosixFileSystemUser


class FSxOpenZFSFileSystemIdentity(BaseModel):
    Type: StrictStr | None = None
    PosixUser: FSxOpenZFSPosixFileSystemUser | None = None
