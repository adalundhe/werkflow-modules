from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedGrafanaListVersionsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    workspaceId: StrictStr | None = None
