from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteMetricCategoryRequest(BaseModel):
    MetricCategoryId: StrictStr
    DryRun: StrictBool | None = None
