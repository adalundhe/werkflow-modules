from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_creation_info import EFSCreationInfo


class EFSRootDirectory(BaseModel):
    Path: StrictStr | None = None
    CreationInfo: EFSCreationInfo | None = None
