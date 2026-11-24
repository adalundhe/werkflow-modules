from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsStopQueryRequest(BaseModel):
    queryId: StrictStr
