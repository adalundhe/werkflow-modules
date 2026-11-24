from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRebuildRequest(BaseModel):
    WorkspaceId: StrictStr
