from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListTrafficPolicyVersionsRequest(BaseModel):
    Id: StrictStr
    TrafficPolicyVersionMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
