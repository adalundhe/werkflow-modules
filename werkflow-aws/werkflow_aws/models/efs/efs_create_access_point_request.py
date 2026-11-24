from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_posix_user import EFSPosixUser
from .efs_root_directory import EFSRootDirectory
from .efs_tag import EFSTag


class EFSCreateAccessPointRequest(BaseModel):
    ClientToken: StrictStr
    FileSystemId: StrictStr
    Tags: list[EFSTag] | None = None
    PosixUser: EFSPosixUser | None = None
    RootDirectory: EFSRootDirectory | None = None
