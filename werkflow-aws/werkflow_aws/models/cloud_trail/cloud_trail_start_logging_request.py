from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStartLoggingRequest(BaseModel):
    Name: StrictStr
