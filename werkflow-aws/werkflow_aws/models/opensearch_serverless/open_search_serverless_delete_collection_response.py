from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_delete_collection_detail import OpenSearchServerlessDeleteCollectionDetail


class OpenSearchServerlessDeleteCollectionResponse(BaseModel):
    deleteCollectionDetail: OpenSearchServerlessDeleteCollectionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
