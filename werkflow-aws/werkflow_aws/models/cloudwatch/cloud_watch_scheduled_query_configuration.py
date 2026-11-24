from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_schedule_configuration import CloudWatchScheduleConfiguration
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchScheduledQueryConfiguration(BaseModel):
    QueryString: StrictStr | None = None
    LogGroupIdentifiers: list[StrictStr] | None = None
    QueryARN: StrictStr | None = None
    ScheduledQueryRoleARN: StrictStr | None = None
    ScheduleConfiguration: CloudWatchScheduleConfiguration | None = None
    AggregationExpression: StrictStr | None = None
    Tags: list[CloudWatchTagModel] | None = None
