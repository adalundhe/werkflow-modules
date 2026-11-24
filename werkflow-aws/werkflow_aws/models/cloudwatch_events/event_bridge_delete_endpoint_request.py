from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeleteEndpointRequest(BaseModel):
    Name: StrictStr
