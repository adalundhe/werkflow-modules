from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_collection_summary import OpenSearchServerlessCollectionSummary


class OpenSearchServerlessListCollectionsResponse(BaseModel):
    collectionSummaries: list[OpenSearchServerlessCollectionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
