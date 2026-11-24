from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_data_source_details import OpenSearchDataSourceDetails


class OpenSearchListDataSourcesResponse(BaseModel):
    DataSources: list[OpenSearchDataSourceDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
