from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteSubscriptionFilterRequest(BaseModel):
    logGroupName: StrictStr
    filterName: StrictStr
