from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_reboot_request import WorkSpacesRebootRequest


class WorkSpacesRebootWorkspacesRequest(BaseModel):
    RebootWorkspaceRequests: list[WorkSpacesRebootRequest]
