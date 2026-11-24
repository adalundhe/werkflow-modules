from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
