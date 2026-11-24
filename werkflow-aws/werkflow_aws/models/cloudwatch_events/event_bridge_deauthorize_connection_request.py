from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeauthorizeConnectionRequest(BaseModel):
    Name: StrictStr
