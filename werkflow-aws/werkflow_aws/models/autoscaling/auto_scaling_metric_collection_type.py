from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingMetricCollectionType(BaseModel):
    Metric: StrictStr | None = None
