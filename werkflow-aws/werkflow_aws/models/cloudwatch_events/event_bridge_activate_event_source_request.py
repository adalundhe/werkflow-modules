from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeActivateEventSourceRequest(BaseModel):
    Name: StrictStr
