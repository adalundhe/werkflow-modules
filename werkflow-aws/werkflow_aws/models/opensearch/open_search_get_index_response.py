from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_index_schema import OpenSearchIndexSchema


class OpenSearchGetIndexResponse(BaseModel):
    IndexSchema: OpenSearchIndexSchema | None = None
    ResponseMetadata: dict[str, Any] | None = None
