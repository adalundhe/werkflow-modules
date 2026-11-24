from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetDataProtectionPolicyRequest(BaseModel):
    logGroupIdentifier: StrictStr
