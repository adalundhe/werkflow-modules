from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamRoutingPolicyRegistrationRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    Cidr: StrictStr
    DryRun: StrictBool | None = None
    Force: StrictBool | None = None
    ClientToken: StrictStr | None = None
