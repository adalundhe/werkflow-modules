from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_metric_dimension import AutoScalingMetricDimension
from .auto_scaling_target_tracking_metric_data_query import AutoScalingTargetTrackingMetricDataQuery


class AutoScalingCustomizedMetricSpecification(BaseModel):
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Dimensions: list[AutoScalingMetricDimension] | None = None
    Statistic: StrictStr | None = None
    Unit: StrictStr | None = None
    Period: StrictInt | None = None
    Metrics: list[AutoScalingTargetTrackingMetricDataQuery] | None = None
