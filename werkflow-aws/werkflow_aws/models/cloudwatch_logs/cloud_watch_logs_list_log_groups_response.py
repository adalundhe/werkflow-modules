from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_log_group_summary import CloudWatchLogsLogGroupSummary


class CloudWatchLogsListLogGroupsResponse(BaseModel):
    logGroups: list[CloudWatchLogsLogGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
