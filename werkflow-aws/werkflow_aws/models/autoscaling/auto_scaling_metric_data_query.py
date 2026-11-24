from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .auto_scaling_metric_stat import AutoScalingMetricStat


class AutoScalingMetricDataQuery(BaseModel):
    Id: StrictStr | None = None
    Expression: StrictStr | None = None
    MetricStat: AutoScalingMetricStat | None = None
    Label: StrictStr | None = None
    ReturnData: StrictBool | None = None
