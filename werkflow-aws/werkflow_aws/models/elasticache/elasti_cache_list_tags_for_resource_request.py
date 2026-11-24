from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheListTagsForResourceRequest(BaseModel):
    ResourceName: StrictStr
