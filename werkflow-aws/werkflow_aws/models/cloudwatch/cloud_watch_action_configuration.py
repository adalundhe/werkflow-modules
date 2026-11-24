from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_alarm_tags_propagation import CloudWatchAlarmTagsPropagation


class CloudWatchActionConfiguration(BaseModel):
    AlarmTagsPropagation: CloudWatchAlarmTagsPropagation | None = None
