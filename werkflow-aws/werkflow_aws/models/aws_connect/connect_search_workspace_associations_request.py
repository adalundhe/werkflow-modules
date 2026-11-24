from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_workspace_association_search_criteria import ConnectWorkspaceAssociationSearchCriteria
from .connect_workspace_association_search_filter import ConnectWorkspaceAssociationSearchFilter


class ConnectSearchWorkspaceAssociationsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectWorkspaceAssociationSearchFilter | None = None
    SearchCriteria: ConnectWorkspaceAssociationSearchCriteria | None = None
