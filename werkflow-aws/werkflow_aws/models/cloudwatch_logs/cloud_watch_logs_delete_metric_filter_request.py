from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteMetricFilterRequest(BaseModel):
    logGroupName: StrictStr
    filterName: StrictStr
