from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .auto_scaling_metric import AutoScalingMetric


class AutoScalingMetricStat(BaseModel):
    Metric: AutoScalingMetric | None = None
    Stat: StrictStr | None = None
    Unit: StrictStr | None = None
