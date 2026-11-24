from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_aggregate_log_group_summary import CloudWatchLogsAggregateLogGroupSummary


class CloudWatchLogsListAggregateLogGroupSummariesResponse(BaseModel):
    aggregateLogGroupSummaries: list[CloudWatchLogsAggregateLogGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
