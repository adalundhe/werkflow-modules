from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedGrafanaCreateWorkspaceApiKeyRequest(BaseModel):
    keyName: StrictStr
    keyRole: StrictStr
    secondsToLive: StrictInt
    workspaceId: StrictStr
