from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteWorkspacePageRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    Page: StrictStr
