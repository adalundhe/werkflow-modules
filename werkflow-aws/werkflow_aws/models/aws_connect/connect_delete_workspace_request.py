from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteWorkspaceRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
