from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_metric_alarm_model import CloudWatchMetricAlarmModel


class CloudWatchDescribeAlarmsForMetricResponse(BaseModel):
    MetricAlarms: list[CloudWatchMetricAlarmModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
