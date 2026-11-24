from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class SecurityHubAwsElbLoadBalancerConnectionDraining(BaseModel):
    Enabled: StrictBool | None = None
    Timeout: StrictInt | None = None
