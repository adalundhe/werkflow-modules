from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudWatchLogsImportFilter(BaseModel):
    startEventTime: StrictInt | None = None
    endEventTime: StrictInt | None = None
