from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_log_group import CloudWatchLogsLogGroup


class CloudWatchLogsDescribeLogGroupsResponse(BaseModel):
    logGroups: list[CloudWatchLogsLogGroup] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
