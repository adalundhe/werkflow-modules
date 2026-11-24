from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateTrafficDistributionGroupUserRequest(BaseModel):
    TrafficDistributionGroupId: StrictStr
    UserId: StrictStr
    InstanceId: StrictStr
