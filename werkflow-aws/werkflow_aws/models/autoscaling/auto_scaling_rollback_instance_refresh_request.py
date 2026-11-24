from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingRollbackInstanceRefreshRequest(BaseModel):
    AutoScalingGroupName: StrictStr
