from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_metric_data_query import AutoScalingMetricDataQuery


class AutoScalingPredictiveScalingCustomizedLoadMetric(BaseModel):
    MetricDataQueries: list[AutoScalingMetricDataQuery] | None = None
