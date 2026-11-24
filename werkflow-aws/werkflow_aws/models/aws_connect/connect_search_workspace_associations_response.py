from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_workspace_association_search_summary import ConnectWorkspaceAssociationSearchSummary


class ConnectSearchWorkspaceAssociationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    WorkspaceAssociations: list[ConnectWorkspaceAssociationSearchSummary] | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
