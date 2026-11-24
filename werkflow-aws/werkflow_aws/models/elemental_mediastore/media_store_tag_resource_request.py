from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .media_store_tag import MediaStoreTag


class MediaStoreTagResourceRequest(BaseModel):
    Resource: StrictStr
    Tags: list[MediaStoreTag]
