from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_workspace_search_summary import ConnectWorkspaceSearchSummary


class ConnectSearchWorkspacesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Workspaces: list[ConnectWorkspaceSearchSummary] | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
