from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubVpcInfoIpv6CidrBlockSetDetails(BaseModel):
    Ipv6CidrBlock: StrictStr | None = None
