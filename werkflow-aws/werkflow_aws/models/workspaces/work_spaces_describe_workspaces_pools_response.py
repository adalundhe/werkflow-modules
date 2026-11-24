from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .workspaces_pool import WorkspacesPool


class WorkSpacesDescribeWorkspacesPoolsResponse(BaseModel):
    WorkspacesPools: list[WorkspacesPool] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
