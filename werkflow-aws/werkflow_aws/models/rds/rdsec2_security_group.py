from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSEC2SecurityGroup(BaseModel):
    Status: StrictStr | None = None
    EC2SecurityGroupName: StrictStr | None = None
    EC2SecurityGroupId: StrictStr | None = None
    EC2SecurityGroupOwnerId: StrictStr | None = None
