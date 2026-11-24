from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElbLoadBalancerSourceSecurityGroup(BaseModel):
    GroupName: StrictStr | None = None
    OwnerAlias: StrictStr | None = None
