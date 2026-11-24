from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_terminate_request import WorkSpacesTerminateRequest


class WorkSpacesTerminateWorkspacesRequest(BaseModel):
    TerminateWorkspaceRequests: list[WorkSpacesTerminateRequest]
