from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchUpdateConsumableResourceRequest(BaseModel):
    consumableResource: StrictStr
    operation: StrictStr | None = None
    quantity: StrictInt | None = None
    clientToken: StrictStr | None = None
