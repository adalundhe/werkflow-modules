from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElbLoadBalancerInstance(BaseModel):
    InstanceId: StrictStr | None = None
