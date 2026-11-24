from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .media_store_tag import MediaStoreTag


class MediaStoreCreateContainerRequest(BaseModel):
    ContainerName: StrictStr
    Tags: list[MediaStoreTag] | None = None
