from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .auto_scaling_metric_dimension import AutoScalingMetricDimension


class AutoScalingMetric(BaseModel):
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[AutoScalingMetricDimension] | None = None
