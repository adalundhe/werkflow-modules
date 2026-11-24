from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_posix_user import EFSPosixUser
from .efs_root_directory import EFSRootDirectory
from .efs_tag import EFSTag


class EFSAccessPointDescription(BaseModel):
    ClientToken: StrictStr | None = None
    Name: StrictStr | None = None
    Tags: list[EFSTag] | None = None
    AccessPointId: StrictStr | None = None
    AccessPointArn: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    PosixUser: EFSPosixUser | None = None
    RootDirectory: EFSRootDirectory | None = None
    OwnerId: StrictStr | None = None
    LifeCycleState: StrictStr | None = None
