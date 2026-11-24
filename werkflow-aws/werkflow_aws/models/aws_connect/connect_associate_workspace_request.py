from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateWorkspaceRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    ResourceArns: list[StrictStr]
