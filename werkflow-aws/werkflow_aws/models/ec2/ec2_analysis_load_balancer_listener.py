from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2AnalysisLoadBalancerListener(BaseModel):
    LoadBalancerPort: StrictInt | None = None
    InstancePort: StrictInt | None = None
