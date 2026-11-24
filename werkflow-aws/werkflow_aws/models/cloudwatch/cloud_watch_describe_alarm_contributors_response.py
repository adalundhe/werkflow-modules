from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_alarm_contributor import CloudWatchAlarmContributor


class CloudWatchDescribeAlarmContributorsResponse(BaseModel):
    AlarmContributors: list[CloudWatchAlarmContributor] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
