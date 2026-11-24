from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTotalAggregationFunction(BaseModel):
    SimpleTotalAggregationFunction: StrictStr | None = None
