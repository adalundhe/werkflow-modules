from __future__ import annotations
from pydantic import BaseModel
from .config_service_stored_query import ConfigServiceStoredQuery
from .config_service_tag import ConfigServiceTag


class ConfigServicePutStoredQueryRequest(BaseModel):
    StoredQuery: ConfigServiceStoredQuery
    Tags: list[ConfigServiceTag] | None = None
