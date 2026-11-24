from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchCreateConsumableResourceRequest(BaseModel):
    consumableResourceName: StrictStr
    totalQuantity: StrictInt | None = None
    resourceType: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
