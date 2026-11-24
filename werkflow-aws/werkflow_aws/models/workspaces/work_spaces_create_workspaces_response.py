from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_failed_create_workspace_request import WorkSpacesFailedCreateWorkspaceRequest
from .work_spaces_workspace import WorkSpacesWorkspace


class WorkSpacesCreateWorkspacesResponse(BaseModel):
    FailedRequests: list[WorkSpacesFailedCreateWorkspaceRequest] | None = None
    PendingRequests: list[WorkSpacesWorkspace] | None = None
    ResponseMetadata: dict[str, Any] | None = None
