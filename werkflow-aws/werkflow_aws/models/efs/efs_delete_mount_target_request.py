from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDeleteMountTargetRequest(BaseModel):
    MountTargetId: StrictStr
