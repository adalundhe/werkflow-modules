from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ssm_alarm import SSMAlarm


class SSMAlarmConfiguration(BaseModel):
    IgnorePollAlarmFailure: StrictBool | None = None
    Alarms: list[SSMAlarm] | None = None
