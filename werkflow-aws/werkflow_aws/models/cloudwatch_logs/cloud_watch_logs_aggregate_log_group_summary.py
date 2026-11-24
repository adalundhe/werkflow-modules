from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_watch_logs_grouping_identifier import CloudWatchLogsGroupingIdentifier


class CloudWatchLogsAggregateLogGroupSummary(BaseModel):
    logGroupCount: StrictInt | None = None
    groupingIdentifiers: list[CloudWatchLogsGroupingIdentifier] | None = None
