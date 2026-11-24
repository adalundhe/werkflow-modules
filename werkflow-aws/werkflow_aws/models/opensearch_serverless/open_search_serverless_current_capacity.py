from __future__ import annotations
from pydantic import BaseModel
from .open_search_serverless_capacity_details import OpenSearchServerlessCapacityDetails


class OpenSearchServerlessCurrentCapacity(BaseModel):
    search: OpenSearchServerlessCapacityDetails | None = None
    indexing: OpenSearchServerlessCapacityDetails | None = None
