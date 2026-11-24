from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsTestMetricFilterRequest(BaseModel):
    filterPattern: StrictStr
    logEventMessages: list[StrictStr]
