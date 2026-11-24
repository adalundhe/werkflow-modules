from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_auto_scaling_policy_state_change_reason import EMRAutoScalingPolicyStateChangeReason


class EMRAutoScalingPolicyStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRAutoScalingPolicyStateChangeReason | None = None
