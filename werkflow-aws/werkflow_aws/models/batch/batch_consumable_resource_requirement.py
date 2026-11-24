from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchConsumableResourceRequirement(BaseModel):
    consumableResource: StrictStr | None = None
    quantity: StrictInt | None = None
