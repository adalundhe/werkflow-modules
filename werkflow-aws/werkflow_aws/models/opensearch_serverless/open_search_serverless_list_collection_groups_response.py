from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_collection_group_summary import OpenSearchServerlessCollectionGroupSummary


class OpenSearchServerlessListCollectionGroupsResponse(BaseModel):
    collectionGroupSummaries: list[OpenSearchServerlessCollectionGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
