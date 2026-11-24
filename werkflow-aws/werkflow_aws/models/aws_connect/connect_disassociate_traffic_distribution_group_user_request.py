from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateTrafficDistributionGroupUserRequest(BaseModel):
    TrafficDistributionGroupId: StrictStr
    UserId: StrictStr
    InstanceId: StrictStr
