from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LightsailMonthlyTransfer(BaseModel):
    gbPerMonthAllocated: StrictInt | None = None
