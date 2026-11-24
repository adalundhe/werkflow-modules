from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDescribeMountTargetSecurityGroupsRequest(BaseModel):
    MountTargetId: StrictStr
