from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_alarm_history_item import CloudWatchAlarmHistoryItem


class CloudWatchDescribeAlarmHistoryResponse(BaseModel):
    AlarmHistoryItems: list[CloudWatchAlarmHistoryItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
