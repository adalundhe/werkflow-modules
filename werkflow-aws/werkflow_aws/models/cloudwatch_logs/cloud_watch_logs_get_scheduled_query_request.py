from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetScheduledQueryRequest(BaseModel):
    identifier: StrictStr
