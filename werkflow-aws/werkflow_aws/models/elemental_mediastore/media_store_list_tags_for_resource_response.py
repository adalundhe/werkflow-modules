from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .media_store_tag import MediaStoreTag


class MediaStoreListTagsForResourceResponse(BaseModel):
    Tags: list[MediaStoreTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
