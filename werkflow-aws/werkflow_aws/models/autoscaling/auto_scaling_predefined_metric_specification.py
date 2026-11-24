from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingPredefinedMetricSpecification(BaseModel):
    PredefinedMetricType: StrictStr | None = None
    ResourceLabel: StrictStr | None = None
