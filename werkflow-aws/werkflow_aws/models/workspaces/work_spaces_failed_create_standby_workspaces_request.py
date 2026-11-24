from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_standby_workspace import WorkSpacesStandbyWorkspace


class WorkSpacesFailedCreateStandbyWorkspacesRequest(BaseModel):
    StandbyWorkspaceRequest: WorkSpacesStandbyWorkspace | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
