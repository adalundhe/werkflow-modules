from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDeleteWorkspaceServiceAccountRequest(BaseModel):
    serviceAccountId: StrictStr
    workspaceId: StrictStr
