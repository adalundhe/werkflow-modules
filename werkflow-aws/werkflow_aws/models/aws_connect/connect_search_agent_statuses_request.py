from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_agent_status_search_criteria import ConnectAgentStatusSearchCriteria
from .connect_agent_status_search_filter import ConnectAgentStatusSearchFilter


class ConnectSearchAgentStatusesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectAgentStatusSearchFilter | None = None
    SearchCriteria: ConnectAgentStatusSearchCriteria | None = None
