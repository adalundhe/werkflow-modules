from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecondarySubnetIpv4CidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
