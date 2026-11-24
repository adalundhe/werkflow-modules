from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_data_table_search_criteria import ConnectDataTableSearchCriteria
from .connect_data_table_search_filter import ConnectDataTableSearchFilter


class ConnectSearchDataTablesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectDataTableSearchFilter | None = None
    SearchCriteria: ConnectDataTableSearchCriteria | None = None
