from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ReservedCapacityFallbackOptions(BaseModel):
    MarketTypes: list[StrictStr] | None = None
