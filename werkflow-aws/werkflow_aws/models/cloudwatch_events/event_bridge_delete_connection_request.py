from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeleteConnectionRequest(BaseModel):
    Name: StrictStr
