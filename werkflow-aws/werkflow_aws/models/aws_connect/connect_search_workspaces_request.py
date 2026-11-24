from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_workspace_search_criteria import ConnectWorkspaceSearchCriteria
from .connect_workspace_search_filter import ConnectWorkspaceSearchFilter


class ConnectSearchWorkspacesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectWorkspaceSearchFilter | None = None
    SearchCriteria: ConnectWorkspaceSearchCriteria | None = None
