from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeCapacityProviderStrategyItem(BaseModel):
    capacityProvider: StrictStr | None = None
    weight: StrictInt | None = None
    base: StrictInt | None = None
