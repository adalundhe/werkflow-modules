from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAggregationListItem(BaseModel):
    attribute: StrictStr
    displayValue: StrictStr | None = None
