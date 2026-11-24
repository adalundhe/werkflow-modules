from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchConsumableResourceSummary(BaseModel):
    consumableResourceArn: StrictStr | None = None
    consumableResourceName: StrictStr | None = None
    totalQuantity: StrictInt | None = None
    inUseQuantity: StrictInt | None = None
    resourceType: StrictStr | None = None
