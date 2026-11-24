from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_index_schema import OpenSearchServerlessIndexSchema


class OpenSearchServerlessUpdateIndexRequest(BaseModel):
    id: StrictStr
    indexName: StrictStr
    indexSchema: OpenSearchServerlessIndexSchema | None = None
