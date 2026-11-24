from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_collection_detail import OpenSearchServerlessCollectionDetail
from .open_search_serverless_collection_error_detail import OpenSearchServerlessCollectionErrorDetail


class OpenSearchServerlessBatchGetCollectionResponse(BaseModel):
    collectionDetails: list[OpenSearchServerlessCollectionDetail] | None = None
    collectionErrorDetails: list[OpenSearchServerlessCollectionErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
