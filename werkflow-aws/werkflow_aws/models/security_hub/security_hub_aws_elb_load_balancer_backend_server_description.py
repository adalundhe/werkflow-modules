from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsElbLoadBalancerBackendServerDescription(BaseModel):
    InstancePort: StrictInt | None = None
    PolicyNames: list[StrictStr] | None = None
