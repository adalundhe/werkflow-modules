from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BatchQuotaShareCapacityUsage(BaseModel):
    capacityUnit: StrictStr | None = None
    quantity: StrictFloat | StrictInt | None = None
