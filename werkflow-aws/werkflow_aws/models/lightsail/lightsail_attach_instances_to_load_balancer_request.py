from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAttachInstancesToLoadBalancerRequest(BaseModel):
    loadBalancerName: StrictStr
    instanceNames: list[StrictStr]
