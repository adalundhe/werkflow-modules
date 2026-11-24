from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDescribeWorkspaceConfigurationRequest(BaseModel):
    workspaceId: StrictStr
