from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsServiceLoadBalancersDetails(BaseModel):
    ContainerName: StrictStr | None = None
    ContainerPort: StrictInt | None = None
    LoadBalancerName: StrictStr | None = None
    TargetGroupArn: StrictStr | None = None
