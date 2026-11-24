from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsPutRetentionPolicyRequest(BaseModel):
    logGroupName: StrictStr
    retentionInDays: StrictInt
