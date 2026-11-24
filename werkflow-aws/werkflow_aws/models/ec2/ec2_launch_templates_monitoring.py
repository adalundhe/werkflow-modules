from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2LaunchTemplatesMonitoring(BaseModel):
    Enabled: StrictBool | None = None
    MetricCategoryIds: list[StrictStr] | None = None
