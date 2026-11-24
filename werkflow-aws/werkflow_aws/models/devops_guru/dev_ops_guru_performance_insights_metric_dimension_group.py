from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DevOpsGuruPerformanceInsightsMetricDimensionGroup(BaseModel):
    Group: StrictStr | None = None
    Dimensions: list[StrictStr] | None = None
    Limit: StrictInt | None = None
