from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightBinCountOptions(BaseModel):
    Value: StrictInt | None = None
