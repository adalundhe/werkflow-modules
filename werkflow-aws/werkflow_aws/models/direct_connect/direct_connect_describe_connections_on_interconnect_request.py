from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDescribeConnectionsOnInterconnectRequest(BaseModel):
    interconnectId: StrictStr
