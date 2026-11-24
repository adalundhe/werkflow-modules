from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingEnabledMetric(BaseModel):
    Metric: StrictStr | None = None
    Granularity: StrictStr | None = None
