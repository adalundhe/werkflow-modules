from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class CloudWatchLogsQueryStatistics(BaseModel):
    recordsMatched: StrictFloat | StrictInt | None = None
    recordsScanned: StrictFloat | StrictInt | None = None
    estimatedRecordsSkipped: StrictFloat | StrictInt | None = None
    bytesScanned: StrictFloat | StrictInt | None = None
    estimatedBytesSkipped: StrictFloat | StrictInt | None = None
    logGroupsScanned: StrictFloat | StrictInt | None = None
    resultCount: StrictFloat | StrictInt | None = None
