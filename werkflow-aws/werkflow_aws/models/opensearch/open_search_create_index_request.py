from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_index_schema import OpenSearchIndexSchema


class OpenSearchCreateIndexRequest(BaseModel):
    DomainName: StrictStr
    IndexName: StrictStr
    IndexSchema: OpenSearchIndexSchema
