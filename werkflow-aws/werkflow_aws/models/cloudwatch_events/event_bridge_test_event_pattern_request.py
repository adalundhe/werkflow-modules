from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeTestEventPatternRequest(BaseModel):
    EventPattern: StrictStr
    Event: StrictStr
