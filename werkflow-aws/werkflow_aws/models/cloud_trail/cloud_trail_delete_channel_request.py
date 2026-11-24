from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDeleteChannelRequest(BaseModel):
    Channel: StrictStr
