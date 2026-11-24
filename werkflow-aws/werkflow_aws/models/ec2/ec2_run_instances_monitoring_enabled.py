from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RunInstancesMonitoringEnabled(BaseModel):
    MetricCategoryIds: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
