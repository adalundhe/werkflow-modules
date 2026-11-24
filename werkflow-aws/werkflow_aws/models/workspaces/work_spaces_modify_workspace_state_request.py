from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesModifyWorkspaceStateRequest(BaseModel):
    WorkspaceId: StrictStr
    WorkspaceState: Literal['AVAILABLE', 'ADMIN_MAINTENANCE']
