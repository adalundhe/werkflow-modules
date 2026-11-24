from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesStartRequest(BaseModel):
    WorkspaceId: StrictStr | None = None
