from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_view_search_criteria import ConnectViewSearchCriteria
from .connect_view_search_filter import ConnectViewSearchFilter


class ConnectSearchViewsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectViewSearchFilter | None = None
    SearchCriteria: ConnectViewSearchCriteria | None = None
