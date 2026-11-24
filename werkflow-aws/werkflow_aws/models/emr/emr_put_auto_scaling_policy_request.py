from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_auto_scaling_policy import EMRAutoScalingPolicy


class EMRPutAutoScalingPolicyRequest(BaseModel):
    ClusterId: StrictStr
    InstanceGroupId: StrictStr
    AutoScalingPolicy: EMRAutoScalingPolicy
