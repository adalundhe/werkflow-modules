from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectListWorkspaceMediaRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
