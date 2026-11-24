from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeWorkspaceRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
