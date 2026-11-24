from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRRemoveAutoScalingPolicyRequest(BaseModel):
    ClusterId: StrictStr
    InstanceGroupId: StrictStr
