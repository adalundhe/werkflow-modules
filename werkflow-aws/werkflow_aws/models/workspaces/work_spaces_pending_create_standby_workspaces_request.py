from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesPendingCreateStandbyWorkspacesRequest(BaseModel):
    UserName: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    State: StrictStr | None = None
    WorkspaceId: StrictStr | None = None
