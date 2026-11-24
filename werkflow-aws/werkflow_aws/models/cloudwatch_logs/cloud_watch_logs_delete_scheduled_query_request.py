from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteScheduledQueryRequest(BaseModel):
    identifier: StrictStr
