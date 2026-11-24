from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListTrafficPoliciesRequest(BaseModel):
    TrafficPolicyIdMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
