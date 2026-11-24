from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRestoreWorkspaceRequest(BaseModel):
    WorkspaceId: StrictStr
