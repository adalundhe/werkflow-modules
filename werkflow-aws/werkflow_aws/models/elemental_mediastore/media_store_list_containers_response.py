from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .media_store_container import MediaStoreContainer


class MediaStoreListContainersResponse(BaseModel):
    Containers: list[MediaStoreContainer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
