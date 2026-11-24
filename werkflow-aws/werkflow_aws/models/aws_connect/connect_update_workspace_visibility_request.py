from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateWorkspaceVisibilityRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    Visibility: Literal['ALL', 'ASSIGNED', 'NONE']
