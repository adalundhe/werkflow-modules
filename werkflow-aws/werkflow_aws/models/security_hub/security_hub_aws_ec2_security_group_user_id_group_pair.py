from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2SecurityGroupUserIdGroupPair(BaseModel):
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    PeeringStatus: StrictStr | None = None
    UserId: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
