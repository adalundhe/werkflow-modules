from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieUsageTotal(BaseModel):
    currency: StrictStr | None = None
    estimatedCost: StrictStr | None = None
    type: StrictStr | None = None
