from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDimensionalPriceRate(BaseModel):
    dimension: StrictStr | None = None
    price: StrictStr | None = None
    description: StrictStr | None = None
    unit: StrictStr | None = None
