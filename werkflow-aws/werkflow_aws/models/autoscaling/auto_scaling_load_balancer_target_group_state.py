from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingLoadBalancerTargetGroupState(BaseModel):
    LoadBalancerTargetGroupARN: StrictStr | None = None
    State: StrictStr | None = None
