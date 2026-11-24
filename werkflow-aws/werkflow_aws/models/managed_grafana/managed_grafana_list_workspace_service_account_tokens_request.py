from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedGrafanaListWorkspaceServiceAccountTokensRequest(BaseModel):
    serviceAccountId: StrictStr
    workspaceId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
