from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutDataProtectionPolicyRequest(BaseModel):
    logGroupIdentifier: StrictStr
    policyDocument: StrictStr
