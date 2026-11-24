from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_direct_query_data_source_type import OpenSearchDirectQueryDataSourceType


class OpenSearchUpdateDirectQueryDataSourceRequest(BaseModel):
    DataSourceName: StrictStr
    DataSourceType: OpenSearchDirectQueryDataSourceType
    Description: StrictStr | None = None
    OpenSearchArns: list[StrictStr] | None = None
    DataSourceAccessPolicy: StrictStr | None = None
