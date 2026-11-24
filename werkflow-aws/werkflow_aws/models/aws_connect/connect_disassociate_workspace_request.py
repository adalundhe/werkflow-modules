from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateWorkspaceRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    ResourceArns: list[StrictStr]
