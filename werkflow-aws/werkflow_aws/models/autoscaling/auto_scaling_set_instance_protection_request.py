from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingSetInstanceProtectionRequest(BaseModel):
    InstanceIds: list[StrictStr]
    AutoScalingGroupName: StrictStr
    ProtectedFromScaleIn: StrictBool
