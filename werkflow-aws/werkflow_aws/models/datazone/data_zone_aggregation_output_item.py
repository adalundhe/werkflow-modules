from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneAggregationOutputItem(BaseModel):
    value: StrictStr | None = None
    count: StrictInt | None = None
    displayValue: StrictStr | None = None
