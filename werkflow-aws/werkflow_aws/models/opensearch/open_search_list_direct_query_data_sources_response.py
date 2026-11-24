from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_direct_query_data_source import OpenSearchDirectQueryDataSource


class OpenSearchListDirectQueryDataSourcesResponse(BaseModel):
    NextToken: StrictStr | None = None
    DirectQueryDataSources: list[OpenSearchDirectQueryDataSource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
