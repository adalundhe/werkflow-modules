from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_update_collection_group_detail import OpenSearchServerlessUpdateCollectionGroupDetail


class OpenSearchServerlessUpdateCollectionGroupResponse(BaseModel):
    updateCollectionGroupDetail: OpenSearchServerlessUpdateCollectionGroupDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
