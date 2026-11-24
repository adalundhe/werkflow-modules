from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyAvailabilityZoneGroupRequest(BaseModel):
    GroupName: StrictStr
    OptInStatus: Literal['opted-in', 'not-opted-in']
    DryRun: StrictBool | None = None
