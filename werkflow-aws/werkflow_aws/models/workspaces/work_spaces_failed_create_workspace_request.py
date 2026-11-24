from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_request import WorkSpacesWorkspaceRequest


class WorkSpacesFailedCreateWorkspaceRequest(BaseModel):
    WorkspaceRequest: WorkSpacesWorkspaceRequest | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
