from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .auto_scaling_predictive_scaling_metric_specification import AutoScalingPredictiveScalingMetricSpecification


class AutoScalingLoadForecast(BaseModel):
    Timestamps: list[datetime.datetime | StrictStr] | None = None
    Values: list[StrictFloat | StrictInt] | None = None
    MetricSpecification: AutoScalingPredictiveScalingMetricSpecification | None = None
