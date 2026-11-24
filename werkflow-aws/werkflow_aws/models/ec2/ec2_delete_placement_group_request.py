from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeletePlacementGroupRequest(BaseModel):
    GroupName: StrictStr
    DryRun: StrictBool | None = None
