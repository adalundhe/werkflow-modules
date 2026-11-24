from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteLogStreamRequest(BaseModel):
    logGroupName: StrictStr
    logStreamName: StrictStr
