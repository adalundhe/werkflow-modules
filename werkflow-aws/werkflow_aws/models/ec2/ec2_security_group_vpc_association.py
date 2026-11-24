from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecurityGroupVpcAssociation(BaseModel):
    GroupId: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcOwnerId: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    GroupOwnerId: StrictStr | None = None
