from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_direct_query_data_source_type import OpenSearchDirectQueryDataSourceType


class OpenSearchGetDirectQueryDataSourceResponse(BaseModel):
    DataSourceName: StrictStr | None = None
    DataSourceType: OpenSearchDirectQueryDataSourceType | None = None
    Description: StrictStr | None = None
    OpenSearchArns: list[StrictStr] | None = None
    DataSourceAccessPolicy: StrictStr | None = None
    DataSourceArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
