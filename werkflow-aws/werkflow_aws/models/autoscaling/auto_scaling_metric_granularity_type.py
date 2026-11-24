from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingMetricGranularityType(BaseModel):
    Granularity: StrictStr | None = None
