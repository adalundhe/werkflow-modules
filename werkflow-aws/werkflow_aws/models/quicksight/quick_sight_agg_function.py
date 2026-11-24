from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAggFunction(BaseModel):
    Aggregation: StrictStr | None = None
    AggregationFunctionParameters: dict[StrictStr, StrictStr] | None = None
    Period: StrictStr | None = None
    PeriodField: StrictStr | None = None
