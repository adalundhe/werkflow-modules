from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteTrafficDistributionGroupRequest(BaseModel):
    TrafficDistributionGroupId: StrictStr
