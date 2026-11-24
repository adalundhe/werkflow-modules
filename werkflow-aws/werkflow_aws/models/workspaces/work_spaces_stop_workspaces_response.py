from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_failed_workspace_change_request import WorkSpacesFailedWorkspaceChangeRequest


class WorkSpacesStopWorkspacesResponse(BaseModel):
    FailedRequests: list[WorkSpacesFailedWorkspaceChangeRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
