from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_alarm import AutoScalingAlarm
from .auto_scaling_predictive_scaling_configuration import AutoScalingPredictiveScalingConfiguration
from .auto_scaling_step_adjustment import AutoScalingStepAdjustment
from .auto_scaling_target_tracking_configuration import AutoScalingTargetTrackingConfiguration


class AutoScalingScalingPolicy(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    PolicyName: StrictStr | None = None
    PolicyARN: StrictStr | None = None
    PolicyType: StrictStr | None = None
    AdjustmentType: StrictStr | None = None
    MinAdjustmentStep: StrictInt | None = None
    MinAdjustmentMagnitude: StrictInt | None = None
    ScalingAdjustment: StrictInt | None = None
    Cooldown: StrictInt | None = None
    StepAdjustments: list[AutoScalingStepAdjustment] | None = None
    MetricAggregationType: StrictStr | None = None
    EstimatedInstanceWarmup: StrictInt | None = None
    Alarms: list[AutoScalingAlarm] | None = None
    TargetTrackingConfiguration: AutoScalingTargetTrackingConfiguration | None = None
    Enabled: StrictBool | None = None
    PredictiveScalingConfiguration: AutoScalingPredictiveScalingConfiguration | None = None
