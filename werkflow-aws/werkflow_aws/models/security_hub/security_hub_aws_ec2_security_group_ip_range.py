from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2SecurityGroupIpRange(BaseModel):
    CidrIp: StrictStr | None = None
