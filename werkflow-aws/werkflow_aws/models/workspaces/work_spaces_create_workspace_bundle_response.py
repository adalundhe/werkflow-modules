from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_workspace_bundle import WorkSpacesWorkspaceBundle


class WorkSpacesCreateWorkspaceBundleResponse(BaseModel):
    WorkspaceBundle: WorkSpacesWorkspaceBundle | None = None
    ResponseMetadata: dict[str, Any] | None = None
