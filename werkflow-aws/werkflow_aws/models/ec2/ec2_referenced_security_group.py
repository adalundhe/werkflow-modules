from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ReferencedSecurityGroup(BaseModel):
    GroupId: StrictStr | None = None
    PeeringStatus: StrictStr | None = None
    UserId: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
