from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetTrailStatusRequest(BaseModel):
    Name: StrictStr
