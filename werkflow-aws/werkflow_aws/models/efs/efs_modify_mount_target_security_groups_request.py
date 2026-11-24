from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSModifyMountTargetSecurityGroupsRequest(BaseModel):
    MountTargetId: StrictStr
    SecurityGroups: list[StrictStr] | None = None
