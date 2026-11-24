from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeEventSourceRequest(BaseModel):
    Name: StrictStr
