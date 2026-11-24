from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteLogGroupRequest(BaseModel):
    logGroupName: StrictStr
