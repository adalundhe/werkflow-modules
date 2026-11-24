from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_alarm_prom_ql_criteria import CloudWatchAlarmPromQLCriteria


class CloudWatchEvaluationCriteria(BaseModel):
    PromQLCriteria: CloudWatchAlarmPromQLCriteria | None = None
