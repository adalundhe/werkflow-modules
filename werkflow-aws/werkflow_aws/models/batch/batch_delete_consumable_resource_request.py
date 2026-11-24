from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeleteConsumableResourceRequest(BaseModel):
    consumableResource: StrictStr
