from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDeleteWorkspaceApiKeyResponse(BaseModel):
    keyName: StrictStr | None = None
    workspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
