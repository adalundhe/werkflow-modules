from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_open_zfs_file_system_identity import FSxOpenZFSFileSystemIdentity


class FSxS3AccessPointOpenZFSConfiguration(BaseModel):
    VolumeId: StrictStr | None = None
    FileSystemIdentity: FSxOpenZFSFileSystemIdentity | None = None
