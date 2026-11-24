from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsTagLogGroupRequest(BaseModel):
    logGroupName: StrictStr
    tags: dict[StrictStr, StrictStr]
