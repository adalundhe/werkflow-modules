from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_workspace_request import WorkSpacesWorkspaceRequest


class WorkSpacesCreateWorkspacesRequest(BaseModel):
    Workspaces: list[WorkSpacesWorkspaceRequest]
