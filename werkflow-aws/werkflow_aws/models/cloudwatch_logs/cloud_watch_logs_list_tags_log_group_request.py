from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsListTagsLogGroupRequest(BaseModel):
    logGroupName: StrictStr
