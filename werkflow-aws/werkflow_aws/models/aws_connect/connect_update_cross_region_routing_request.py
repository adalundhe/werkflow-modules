from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectUpdateCrossRegionRoutingRequest(BaseModel):
    InstanceId: StrictStr
    IsolatedAll: StrictBool
