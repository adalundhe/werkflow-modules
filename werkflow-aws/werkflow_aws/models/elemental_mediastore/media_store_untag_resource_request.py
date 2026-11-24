from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreUntagResourceRequest(BaseModel):
    Resource: StrictStr
    TagKeys: list[StrictStr]
