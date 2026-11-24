from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeactivateEventSourceRequest(BaseModel):
    Name: StrictStr
