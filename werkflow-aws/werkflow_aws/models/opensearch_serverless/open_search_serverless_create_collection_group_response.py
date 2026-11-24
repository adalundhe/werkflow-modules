from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_create_collection_group_detail import OpenSearchServerlessCreateCollectionGroupDetail


class OpenSearchServerlessCreateCollectionGroupResponse(BaseModel):
    createCollectionGroupDetail: OpenSearchServerlessCreateCollectionGroupDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
