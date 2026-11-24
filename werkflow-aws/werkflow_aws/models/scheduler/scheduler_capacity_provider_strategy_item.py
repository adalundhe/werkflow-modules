from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SchedulerCapacityProviderStrategyItem(BaseModel):
    capacityProvider: StrictStr | None = None
    weight: StrictInt | None = None
    base: StrictInt | None = None
