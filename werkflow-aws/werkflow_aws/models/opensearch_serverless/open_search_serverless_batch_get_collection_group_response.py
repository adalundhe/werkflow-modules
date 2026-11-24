from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_collection_group_detail import OpenSearchServerlessCollectionGroupDetail
from .open_search_serverless_collection_group_error_detail import OpenSearchServerlessCollectionGroupErrorDetail


class OpenSearchServerlessBatchGetCollectionGroupResponse(BaseModel):
    collectionGroupDetails: list[OpenSearchServerlessCollectionGroupDetail] | None = None
    collectionGroupErrorDetails: list[OpenSearchServerlessCollectionGroupErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
