from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
