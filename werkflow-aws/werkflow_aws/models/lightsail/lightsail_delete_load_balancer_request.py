from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteLoadBalancerRequest(BaseModel):
    loadBalancerName: StrictStr
