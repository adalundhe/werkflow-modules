from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateWorkspaceMetadataRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Title: StrictStr | None = None
