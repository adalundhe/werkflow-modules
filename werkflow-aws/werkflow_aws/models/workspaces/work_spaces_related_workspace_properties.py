from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRelatedWorkspaceProperties(BaseModel):
    WorkspaceId: StrictStr | None = None
    Region: StrictStr | None = None
    State: StrictStr | None = None
    Type: StrictStr | None = None
