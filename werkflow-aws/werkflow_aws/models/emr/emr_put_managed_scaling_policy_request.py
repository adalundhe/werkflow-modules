from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_managed_scaling_policy import EMRManagedScalingPolicy


class EMRPutManagedScalingPolicyRequest(BaseModel):
    ClusterId: StrictStr
    ManagedScalingPolicy: EMRManagedScalingPolicy
