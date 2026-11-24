from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkSpacesDeployWorkspaceApplicationsRequest(BaseModel):
    WorkspaceId: StrictStr
    Force: StrictBool | None = None
