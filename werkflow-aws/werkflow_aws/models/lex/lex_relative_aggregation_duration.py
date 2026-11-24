from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexRelativeAggregationDuration(BaseModel):
    timeDimension: StrictStr | None = None
    timeValue: StrictInt | None = None
