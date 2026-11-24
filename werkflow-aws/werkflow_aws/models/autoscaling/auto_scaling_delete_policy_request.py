from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDeletePolicyRequest(BaseModel):
    PolicyName: StrictStr
    AutoScalingGroupName: StrictStr | None = None
