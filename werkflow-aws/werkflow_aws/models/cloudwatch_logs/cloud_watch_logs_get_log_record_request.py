from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsGetLogRecordRequest(BaseModel):
    logRecordPointer: StrictStr
    unmask: StrictBool | None = None
