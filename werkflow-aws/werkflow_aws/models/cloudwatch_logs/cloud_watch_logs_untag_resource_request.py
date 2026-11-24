from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
