from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRebootRequest(BaseModel):
    WorkspaceId: StrictStr
