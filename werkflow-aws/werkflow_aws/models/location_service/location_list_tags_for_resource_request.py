from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
