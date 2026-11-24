from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53TrafficPolicySummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    LatestVersion: StrictInt | None = None
    TrafficPolicyCount: StrictInt | None = None
