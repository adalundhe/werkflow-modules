from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_stop_request import WorkSpacesStopRequest


class WorkSpacesStopWorkspacesRequest(BaseModel):
    StopWorkspaceRequests: list[WorkSpacesStopRequest]
