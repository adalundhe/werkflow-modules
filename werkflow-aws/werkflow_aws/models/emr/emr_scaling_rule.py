from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_scaling_action import EMRScalingAction
from .emr_scaling_trigger import EMRScalingTrigger


class EMRScalingRule(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Action: EMRScalingAction | None = None
    Trigger: EMRScalingTrigger | None = None
