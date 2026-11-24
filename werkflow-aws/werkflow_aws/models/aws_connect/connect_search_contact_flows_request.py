from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_contact_flow_search_criteria import ConnectContactFlowSearchCriteria
from .connect_contact_flow_search_filter import ConnectContactFlowSearchFilter


class ConnectSearchContactFlowsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectContactFlowSearchFilter | None = None
    SearchCriteria: ConnectContactFlowSearchCriteria | None = None
