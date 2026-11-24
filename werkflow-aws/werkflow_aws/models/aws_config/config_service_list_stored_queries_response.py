from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_stored_query_metadata import ConfigServiceStoredQueryMetadata


class ConfigServiceListStoredQueriesResponse(BaseModel):
    StoredQueryMetadata: list[ConfigServiceStoredQueryMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
