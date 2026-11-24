from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRSimpleScalingPolicyConfiguration(BaseModel):
    AdjustmentType: StrictStr | None = None
    ScalingAdjustment: StrictInt | None = None
    CoolDown: StrictInt | None = None
