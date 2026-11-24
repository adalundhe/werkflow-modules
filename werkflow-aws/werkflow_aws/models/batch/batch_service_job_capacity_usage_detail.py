from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BatchServiceJobCapacityUsageDetail(BaseModel):
    capacityUnit: StrictStr | None = None
    quantity: StrictFloat | StrictInt | None = None
