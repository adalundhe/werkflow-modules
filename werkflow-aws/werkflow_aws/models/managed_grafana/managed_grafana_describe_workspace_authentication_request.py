from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDescribeWorkspaceAuthenticationRequest(BaseModel):
    workspaceId: StrictStr
