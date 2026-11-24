from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheRemoveTagsFromResourceRequest(BaseModel):
    ResourceName: StrictStr
    TagKeys: list[StrictStr]
