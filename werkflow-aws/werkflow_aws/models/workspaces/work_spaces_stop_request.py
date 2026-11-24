from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesStopRequest(BaseModel):
    WorkspaceId: StrictStr | None = None
