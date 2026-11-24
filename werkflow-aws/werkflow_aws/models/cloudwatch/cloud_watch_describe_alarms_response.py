from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_composite_alarm import CloudWatchCompositeAlarm
from .cloud_watch_metric_alarm import CloudWatchMetricAlarm


class CloudWatchDescribeAlarmsResponse(BaseModel):
    CompositeAlarms: list[CloudWatchCompositeAlarm] | None = None
    MetricAlarms: list[CloudWatchMetricAlarm] | None = None
    NextToken: StrictStr | None = None
