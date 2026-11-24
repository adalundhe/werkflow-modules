from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53TrafficPolicyInstance(BaseModel):
    Id: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    Name: StrictStr | None = None
    TTL: StrictInt | None = None
    State: StrictStr | None = None
    Message: StrictStr | None = None
    TrafficPolicyId: StrictStr | None = None
    TrafficPolicyVersion: StrictInt | None = None
    TrafficPolicyType: StrictStr | None = None
