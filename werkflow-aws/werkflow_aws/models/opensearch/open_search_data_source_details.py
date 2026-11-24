from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_data_source_type import OpenSearchDataSourceType


class OpenSearchDataSourceDetails(BaseModel):
    DataSourceType: OpenSearchDataSourceType | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
