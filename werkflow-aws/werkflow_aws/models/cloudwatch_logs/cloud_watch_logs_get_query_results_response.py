from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_query_statistics import CloudWatchLogsQueryStatistics
from .cloud_watch_logs_result_field import CloudWatchLogsResultField


class CloudWatchLogsGetQueryResultsResponse(BaseModel):
    queryLanguage: StrictStr | None = None
    results: list[list[CloudWatchLogsResultField]] | None = None
    statistics: CloudWatchLogsQueryStatistics | None = None
    status: StrictStr | None = None
    encryptionKey: StrictStr | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
