from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetCrossRegionRoutingRequest(BaseModel):
    InstanceId: StrictStr
