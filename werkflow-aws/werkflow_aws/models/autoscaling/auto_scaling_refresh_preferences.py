from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_alarm_specification import AutoScalingAlarmSpecification


class AutoScalingRefreshPreferences(BaseModel):
    MinHealthyPercentage: StrictInt | None = None
    InstanceWarmup: StrictInt | None = None
    CheckpointPercentages: list[StrictInt] | None = None
    CheckpointDelay: StrictInt | None = None
    SkipMatching: StrictBool | None = None
    AutoRollback: StrictBool | None = None
    ScaleInProtectedInstances: StrictStr | None = None
    StandbyInstances: StrictStr | None = None
    AlarmSpecification: AutoScalingAlarmSpecification | None = None
    MaxHealthyPercentage: StrictInt | None = None
    BakeTime: StrictInt | None = None
