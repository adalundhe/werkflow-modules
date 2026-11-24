from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
