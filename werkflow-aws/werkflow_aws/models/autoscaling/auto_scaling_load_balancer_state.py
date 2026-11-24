from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingLoadBalancerState(BaseModel):
    LoadBalancerName: StrictStr | None = None
    State: StrictStr | None = None
