from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedGrafanaCreateWorkspaceServiceAccountTokenRequest(BaseModel):
    name: StrictStr
    secondsToLive: StrictInt
    serviceAccountId: StrictStr
    workspaceId: StrictStr
