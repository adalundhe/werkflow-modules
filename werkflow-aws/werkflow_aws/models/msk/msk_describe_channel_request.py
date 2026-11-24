from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeChannelRequest(BaseModel):
    ChannelArn: StrictStr
    ClusterArn: StrictStr
