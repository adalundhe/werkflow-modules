from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from .auto_scaling_customized_metric_specification import AutoScalingCustomizedMetricSpecification
from .auto_scaling_predefined_metric_specification import AutoScalingPredefinedMetricSpecification


class AutoScalingTargetTrackingConfiguration(BaseModel):
    PredefinedMetricSpecification: AutoScalingPredefinedMetricSpecification | None = None
    CustomizedMetricSpecification: AutoScalingCustomizedMetricSpecification | None = None
    TargetValue: StrictFloat | StrictInt | None = None
    DisableScaleIn: StrictBool | None = None
