from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class AutoScalingExecutePolicyRequest(BaseModel):
    PolicyName: StrictStr
    AutoScalingGroupName: StrictStr | None = None
    HonorCooldown: StrictBool | None = None
    MetricValue: StrictFloat | StrictInt | None = None
    BreachThreshold: StrictFloat | StrictInt | None = None
