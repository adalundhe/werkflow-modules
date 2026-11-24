from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsOutputLogEvent(BaseModel):
    timestamp: StrictInt | None = None
    message: StrictStr | None = None
    ingestionTime: StrictInt | None = None
