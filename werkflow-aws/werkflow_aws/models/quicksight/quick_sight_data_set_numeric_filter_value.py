from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightDataSetNumericFilterValue(BaseModel):
    StaticValue: StrictFloat | StrictInt | None = None
