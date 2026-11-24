from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsPutLogGroupDeletionProtectionRequest(BaseModel):
    logGroupIdentifier: StrictStr
    deletionProtectionEnabled: StrictBool
