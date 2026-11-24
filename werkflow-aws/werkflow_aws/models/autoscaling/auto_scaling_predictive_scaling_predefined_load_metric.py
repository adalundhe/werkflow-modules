from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingPredictiveScalingPredefinedLoadMetric(BaseModel):
    PredefinedMetricType: StrictStr | None = None
    ResourceLabel: StrictStr | None = None
