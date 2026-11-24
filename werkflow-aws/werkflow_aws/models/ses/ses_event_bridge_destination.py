from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESEventBridgeDestination(BaseModel):
    EventBusArn: StrictStr | None = None
