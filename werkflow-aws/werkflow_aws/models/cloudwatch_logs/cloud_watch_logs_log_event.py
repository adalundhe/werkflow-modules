from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLogEvent(BaseModel):
    timestamp: StrictInt | None = None
    message: StrictStr | None = None
