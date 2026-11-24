from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_target_tracking_metric_stat import AutoScalingTargetTrackingMetricStat


class AutoScalingTargetTrackingMetricDataQuery(BaseModel):
    Id: StrictStr | None = None
    Expression: StrictStr | None = None
    MetricStat: AutoScalingTargetTrackingMetricStat | None = None
    Label: StrictStr | None = None
    Period: StrictInt | None = None
    ReturnData: StrictBool | None = None
