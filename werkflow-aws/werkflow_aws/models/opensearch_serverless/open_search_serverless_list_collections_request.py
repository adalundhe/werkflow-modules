from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_collection_filters import OpenSearchServerlessCollectionFilters


class OpenSearchServerlessListCollectionsRequest(BaseModel):
    collectionFilters: OpenSearchServerlessCollectionFilters | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
