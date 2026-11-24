from __future__ import annotations
from pydantic import BaseModel
from .emr_auto_scaling_policy_status import EMRAutoScalingPolicyStatus
from .emr_scaling_constraints import EMRScalingConstraints
from .emr_scaling_rule import EMRScalingRule


class EMRAutoScalingPolicyDescription(BaseModel):
    Status: EMRAutoScalingPolicyStatus | None = None
    Constraints: EMRScalingConstraints | None = None
    Rules: list[EMRScalingRule] | None = None
