from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .sage_maker_metric_specification import SageMakerMetricSpecification


class SageMakerTargetTrackingScalingPolicyConfiguration(BaseModel):
    MetricSpecification: SageMakerMetricSpecification | None = None
    TargetValue: StrictFloat | StrictInt | None = None
