from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsElbLoadBalancerCrossZoneLoadBalancing(BaseModel):
    Enabled: StrictBool | None = None
