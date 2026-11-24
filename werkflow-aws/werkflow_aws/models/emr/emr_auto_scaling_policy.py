from __future__ import annotations
from pydantic import BaseModel
from .emr_scaling_constraints import EMRScalingConstraints
from .emr_scaling_rule import EMRScalingRule


class EMRAutoScalingPolicy(BaseModel):
    Constraints: EMRScalingConstraints
    Rules: list[EMRScalingRule]
