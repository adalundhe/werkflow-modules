from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutIndexPolicyRequest(BaseModel):
    logGroupIdentifier: StrictStr
    policyDocument: StrictStr
