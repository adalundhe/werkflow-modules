from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeEventBusRequest(BaseModel):
    Name: StrictStr | None = None
