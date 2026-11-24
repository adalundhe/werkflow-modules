from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KendraCapacityUnitsConfiguration(BaseModel):
    StorageCapacityUnits: StrictInt | None = None
    QueryCapacityUnits: StrictInt | None = None
