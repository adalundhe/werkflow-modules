from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_metric import AutoScalingMetric


class AutoScalingTargetTrackingMetricStat(BaseModel):
    Metric: AutoScalingMetric | None = None
    Stat: StrictStr | None = None
    Unit: StrictStr | None = None
    Period: StrictInt | None = None
