from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyMetricCategoryRequest(BaseModel):
    MetricCategoryId: StrictStr
    Metrics: list[StrictStr]
    DryRun: StrictBool | None = None
