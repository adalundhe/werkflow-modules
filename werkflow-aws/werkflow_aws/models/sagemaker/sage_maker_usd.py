from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerUSD(BaseModel):
    Dollars: StrictInt | None = None
    Cents: StrictInt | None = None
    TenthFractionsOfACent: StrictInt | None = None
