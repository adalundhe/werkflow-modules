from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
