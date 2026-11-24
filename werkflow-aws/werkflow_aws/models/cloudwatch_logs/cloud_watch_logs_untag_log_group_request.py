from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsUntagLogGroupRequest(BaseModel):
    logGroupName: StrictStr
    tags: list[StrictStr]
