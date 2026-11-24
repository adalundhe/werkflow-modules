from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_predictive_scaling_metric_specification import AutoScalingPredictiveScalingMetricSpecification


class AutoScalingPredictiveScalingConfiguration(BaseModel):
    MetricSpecifications: list[AutoScalingPredictiveScalingMetricSpecification] | None = None
    Mode: StrictStr | None = None
    SchedulingBufferTime: StrictInt | None = None
    MaxCapacityBreachBehavior: StrictStr | None = None
    MaxCapacityBuffer: StrictInt | None = None
