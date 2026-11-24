from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_stored_query import ConfigServiceStoredQuery


class ConfigServiceGetStoredQueryResponse(BaseModel):
    StoredQuery: ConfigServiceStoredQuery | None = None
    ResponseMetadata: dict[str, Any] | None = None
