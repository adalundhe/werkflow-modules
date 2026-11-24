from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UserIdGroupPair(BaseModel):
    Description: StrictStr | None = None
    UserId: StrictStr | None = None
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    PeeringStatus: StrictStr | None = None
