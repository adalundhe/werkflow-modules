from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudWatchLogsExportTaskExecutionInfo(BaseModel):
    creationTime: StrictInt | None = None
    completionTime: StrictInt | None = None
