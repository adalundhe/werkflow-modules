from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_scheduled_query_summary import CloudWatchLogsScheduledQuerySummary


class CloudWatchLogsListScheduledQueriesResponse(BaseModel):
    nextToken: StrictStr | None = None
    scheduledQueries: list[CloudWatchLogsScheduledQuerySummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
