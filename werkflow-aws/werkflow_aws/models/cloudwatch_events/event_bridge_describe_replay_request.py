from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeReplayRequest(BaseModel):
    ReplayName: StrictStr
