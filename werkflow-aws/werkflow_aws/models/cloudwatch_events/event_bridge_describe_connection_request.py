from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeConnectionRequest(BaseModel):
    Name: StrictStr
