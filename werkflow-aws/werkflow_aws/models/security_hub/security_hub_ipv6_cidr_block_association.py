from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubIpv6CidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    CidrBlockState: StrictStr | None = None
