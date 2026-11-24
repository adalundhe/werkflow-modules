from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_index_schema import OpenSearchServerlessIndexSchema


class OpenSearchServerlessGetIndexResponse(BaseModel):
    indexSchema: OpenSearchServerlessIndexSchema | None = None
    ResponseMetadata: dict[str, Any] | None = None
