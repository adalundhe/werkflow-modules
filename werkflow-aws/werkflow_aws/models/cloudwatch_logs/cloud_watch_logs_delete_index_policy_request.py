from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteIndexPolicyRequest(BaseModel):
    logGroupIdentifier: StrictStr
