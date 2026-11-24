from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailAggregationConfiguration(BaseModel):
    Templates: list[StrictStr] | None = None
    EventCategory: StrictStr | None = None
