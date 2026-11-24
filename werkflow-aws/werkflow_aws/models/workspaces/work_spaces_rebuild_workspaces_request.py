from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_rebuild_request import WorkSpacesRebuildRequest


class WorkSpacesRebuildWorkspacesRequest(BaseModel):
    RebuildWorkspaceRequests: list[WorkSpacesRebuildRequest]
