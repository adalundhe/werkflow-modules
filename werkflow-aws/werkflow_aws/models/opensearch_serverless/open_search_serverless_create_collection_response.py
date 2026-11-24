from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_create_collection_detail import OpenSearchServerlessCreateCollectionDetail


class OpenSearchServerlessCreateCollectionResponse(BaseModel):
    createCollectionDetail: OpenSearchServerlessCreateCollectionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
