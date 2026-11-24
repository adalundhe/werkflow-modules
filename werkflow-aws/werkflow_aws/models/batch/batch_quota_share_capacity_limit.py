from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchQuotaShareCapacityLimit(BaseModel):
    maxCapacity: StrictInt | None = None
    capacityUnit: StrictStr | None = None
