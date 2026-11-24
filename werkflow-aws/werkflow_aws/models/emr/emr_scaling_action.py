from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_simple_scaling_policy_configuration import EMRSimpleScalingPolicyConfiguration


class EMRScalingAction(BaseModel):
    Market: StrictStr | None = None
    SimpleScalingPolicyConfiguration: EMRSimpleScalingPolicyConfiguration | None = None
