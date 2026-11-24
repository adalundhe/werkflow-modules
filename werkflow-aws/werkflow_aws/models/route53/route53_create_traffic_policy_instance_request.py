from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53CreateTrafficPolicyInstanceRequest(BaseModel):
    HostedZoneId: StrictStr
    Name: StrictStr
    TTL: StrictInt
    TrafficPolicyId: StrictStr
    TrafficPolicyVersion: StrictInt
