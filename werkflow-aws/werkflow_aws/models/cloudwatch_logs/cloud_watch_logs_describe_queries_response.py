from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_query_info import CloudWatchLogsQueryInfo


class CloudWatchLogsDescribeQueriesResponse(BaseModel):
    queries: list[CloudWatchLogsQueryInfo] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
