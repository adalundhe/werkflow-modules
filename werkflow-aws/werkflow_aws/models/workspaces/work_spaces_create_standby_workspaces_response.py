from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_failed_create_standby_workspaces_request import WorkSpacesFailedCreateStandbyWorkspacesRequest
from .work_spaces_pending_create_standby_workspaces_request import WorkSpacesPendingCreateStandbyWorkspacesRequest


class WorkSpacesCreateStandbyWorkspacesResponse(BaseModel):
    FailedStandbyRequests: list[WorkSpacesFailedCreateStandbyWorkspacesRequest] | None = None
    PendingStandbyRequests: list[WorkSpacesPendingCreateStandbyWorkspacesRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
