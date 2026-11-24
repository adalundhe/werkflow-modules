from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingDeleteWarmPoolRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ForceDelete: StrictBool | None = None
