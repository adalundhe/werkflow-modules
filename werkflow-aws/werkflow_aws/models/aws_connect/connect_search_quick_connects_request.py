from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_quick_connect_search_criteria import ConnectQuickConnectSearchCriteria
from .connect_quick_connect_search_filter import ConnectQuickConnectSearchFilter


class ConnectSearchQuickConnectsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectQuickConnectSearchFilter | None = None
    SearchCriteria: ConnectQuickConnectSearchCriteria | None = None
