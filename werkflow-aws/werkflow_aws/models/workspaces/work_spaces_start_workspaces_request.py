from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_start_request import WorkSpacesStartRequest


class WorkSpacesStartWorkspacesRequest(BaseModel):
    StartWorkspaceRequests: list[WorkSpacesStartRequest]
