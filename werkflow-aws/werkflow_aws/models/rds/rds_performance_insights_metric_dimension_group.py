from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSPerformanceInsightsMetricDimensionGroup(BaseModel):
    Dimensions: list[StrictStr] | None = None
    Group: StrictStr | None = None
    Limit: StrictInt | None = None
