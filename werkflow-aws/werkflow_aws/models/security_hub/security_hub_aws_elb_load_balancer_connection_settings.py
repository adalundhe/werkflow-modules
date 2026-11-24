from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsElbLoadBalancerConnectionSettings(BaseModel):
    IdleTimeout: StrictInt | None = None
