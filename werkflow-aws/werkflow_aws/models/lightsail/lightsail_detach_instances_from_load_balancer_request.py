from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDetachInstancesFromLoadBalancerRequest(BaseModel):
    loadBalancerName: StrictStr
    instanceNames: list[StrictStr]
