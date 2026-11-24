from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsElbLoadBalancerHealthCheck(BaseModel):
    HealthyThreshold: StrictInt | None = None
    Interval: StrictInt | None = None
    Target: StrictStr | None = None
    Timeout: StrictInt | None = None
    UnhealthyThreshold: StrictInt | None = None
