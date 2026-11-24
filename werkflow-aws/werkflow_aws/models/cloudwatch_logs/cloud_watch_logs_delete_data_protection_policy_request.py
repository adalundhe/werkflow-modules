from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteDataProtectionPolicyRequest(BaseModel):
    logGroupIdentifier: StrictStr
