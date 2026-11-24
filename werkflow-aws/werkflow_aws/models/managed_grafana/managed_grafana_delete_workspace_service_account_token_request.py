from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDeleteWorkspaceServiceAccountTokenRequest(BaseModel):
    tokenId: StrictStr
    serviceAccountId: StrictStr
    workspaceId: StrictStr
