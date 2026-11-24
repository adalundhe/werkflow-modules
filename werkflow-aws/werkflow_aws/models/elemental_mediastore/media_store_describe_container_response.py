from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .media_store_container import MediaStoreContainer


class MediaStoreDescribeContainerResponse(BaseModel):
    Container: MediaStoreContainer | None = None
    ResponseMetadata: dict[str, Any] | None = None
