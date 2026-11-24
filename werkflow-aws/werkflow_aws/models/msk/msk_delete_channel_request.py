from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteChannelRequest(BaseModel):
    ChannelArn: StrictStr
    ClusterArn: StrictStr
