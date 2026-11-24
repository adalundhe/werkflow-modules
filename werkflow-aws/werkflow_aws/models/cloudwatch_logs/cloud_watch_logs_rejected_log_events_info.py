from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudWatchLogsRejectedLogEventsInfo(BaseModel):
    tooNewLogEventStartIndex: StrictInt | None = None
    tooOldLogEventEndIndex: StrictInt | None = None
    expiredLogEventEndIndex: StrictInt | None = None
