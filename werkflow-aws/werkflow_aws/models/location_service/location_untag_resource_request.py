from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
