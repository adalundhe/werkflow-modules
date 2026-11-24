from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_user_search_criteria import ConnectUserSearchCriteria
from .connect_user_search_filter import ConnectUserSearchFilter


class ConnectSearchUsersRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectUserSearchFilter | None = None
    SearchCriteria: ConnectUserSearchCriteria | None = None
