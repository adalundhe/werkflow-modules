from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2MonetizeAction(BaseModel):
    PriceMultiplier: StrictStr | None = None
