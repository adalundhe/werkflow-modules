from __future__ import annotations
from pydantic import BaseModel
from .emr_cloud_watch_alarm_definition import EMRCloudWatchAlarmDefinition


class EMRScalingTrigger(BaseModel):
    CloudWatchAlarmDefinition: EMRCloudWatchAlarmDefinition | None = None
