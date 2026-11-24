from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_update_collection_detail import OpenSearchServerlessUpdateCollectionDetail


class OpenSearchServerlessUpdateCollectionResponse(BaseModel):
    updateCollectionDetail: OpenSearchServerlessUpdateCollectionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
