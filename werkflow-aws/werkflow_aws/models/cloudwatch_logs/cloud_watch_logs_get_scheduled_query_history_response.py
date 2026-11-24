from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_trigger_history_record import CloudWatchLogsTriggerHistoryRecord


class CloudWatchLogsGetScheduledQueryHistoryResponse(BaseModel):
    name: StrictStr | None = None
    scheduledQueryArn: StrictStr | None = None
    triggerHistory: list[CloudWatchLogsTriggerHistoryRecord] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
