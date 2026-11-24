from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetTrailRequest(BaseModel):
    Name: StrictStr
