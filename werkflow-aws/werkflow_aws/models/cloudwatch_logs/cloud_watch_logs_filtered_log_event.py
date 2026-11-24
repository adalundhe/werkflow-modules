from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsFilteredLogEvent(BaseModel):
    logStreamName: StrictStr | None = None
    timestamp: StrictInt | None = None
    message: StrictStr | None = None
    ingestionTime: StrictInt | None = None
    eventId: StrictStr | None = None
