from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteRetentionPolicyRequest(BaseModel):
    logGroupName: StrictStr
