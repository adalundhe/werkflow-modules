from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLiveTailSessionLogEvent(BaseModel):
    logStreamName: StrictStr | None = None
    logGroupIdentifier: StrictStr | None = None
    message: StrictStr | None = None
    timestamp: StrictInt | None = None
    ingestionTime: StrictInt | None = None
