from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BatchFairshareCapacityUsage(BaseModel):
    capacityUnit: StrictStr | None = None
    quantity: StrictFloat | StrictInt | None = None
