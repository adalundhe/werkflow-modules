from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeEndpointEventBus(BaseModel):
    EventBusArn: StrictStr | None = None
