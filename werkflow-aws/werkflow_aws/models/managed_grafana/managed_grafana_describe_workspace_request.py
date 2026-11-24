from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDescribeWorkspaceRequest(BaseModel):
    workspaceId: StrictStr
