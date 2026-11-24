from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2SecurityGroupIpv6Range(BaseModel):
    CidrIpv6: StrictStr | None = None
