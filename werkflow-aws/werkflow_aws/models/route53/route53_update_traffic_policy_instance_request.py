from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53UpdateTrafficPolicyInstanceRequest(BaseModel):
    Id: StrictStr
    TTL: StrictInt
    TrafficPolicyId: StrictStr
    TrafficPolicyVersion: StrictInt
