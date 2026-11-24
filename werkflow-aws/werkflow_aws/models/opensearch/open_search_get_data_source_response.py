from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_data_source_type import OpenSearchDataSourceType


class OpenSearchGetDataSourceResponse(BaseModel):
    DataSourceType: OpenSearchDataSourceType | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
