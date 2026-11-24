from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeTrafficDistributionGroupRequest(BaseModel):
    TrafficDistributionGroupId: StrictStr
