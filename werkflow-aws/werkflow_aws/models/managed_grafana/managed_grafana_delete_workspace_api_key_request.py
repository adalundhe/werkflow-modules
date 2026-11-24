from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDeleteWorkspaceApiKeyRequest(BaseModel):
    keyName: StrictStr
    workspaceId: StrictStr
