from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2CreateIpamRoutingPolicyRegistrationRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    Cidr: StrictStr
    Asns: list[StrictStr]
    DryRun: StrictBool | None = None
    PermitMoreSpecificAnnouncements: StrictBool | None = None
    MaxLength: StrictInt | None = None
    Description: StrictStr | None = None
    Force: StrictBool | None = None
    ClientToken: StrictStr | None = None
