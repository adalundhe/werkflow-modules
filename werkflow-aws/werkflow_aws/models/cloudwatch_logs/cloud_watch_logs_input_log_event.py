from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsInputLogEvent(BaseModel):
    timestamp: StrictInt
    message: StrictStr
