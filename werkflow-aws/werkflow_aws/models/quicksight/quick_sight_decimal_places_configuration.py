from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightDecimalPlacesConfiguration(BaseModel):
    DecimalPlaces: StrictInt | None = None
