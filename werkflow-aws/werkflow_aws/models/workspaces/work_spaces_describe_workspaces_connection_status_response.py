from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_connection_status import WorkSpacesWorkspaceConnectionStatus


class WorkSpacesDescribeWorkspacesConnectionStatusResponse(BaseModel):
    WorkspacesConnectionStatus: list[WorkSpacesWorkspaceConnectionStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
