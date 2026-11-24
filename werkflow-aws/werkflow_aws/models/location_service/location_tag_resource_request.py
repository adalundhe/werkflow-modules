from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr]
