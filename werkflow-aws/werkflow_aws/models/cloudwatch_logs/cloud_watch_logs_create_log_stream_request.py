from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCreateLogStreamRequest(BaseModel):
    logGroupName: StrictStr
    logStreamName: StrictStr
