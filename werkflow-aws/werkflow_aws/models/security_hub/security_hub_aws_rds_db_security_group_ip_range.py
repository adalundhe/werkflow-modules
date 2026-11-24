from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbSecurityGroupIpRange(BaseModel):
    CidrIp: StrictStr | None = None
    Status: StrictStr | None = None
