from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetChannelRequest(BaseModel):
    Channel: StrictStr
