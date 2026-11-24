from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStopLoggingRequest(BaseModel):
    Name: StrictStr
