from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_contact_flow_module_search_criteria import ConnectContactFlowModuleSearchCriteria
from .connect_contact_flow_module_search_filter import ConnectContactFlowModuleSearchFilter


class ConnectSearchContactFlowModulesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectContactFlowModuleSearchFilter | None = None
    SearchCriteria: ConnectContactFlowModuleSearchCriteria | None = None
