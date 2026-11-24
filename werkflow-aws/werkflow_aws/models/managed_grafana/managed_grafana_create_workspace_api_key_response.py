from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedGrafanaCreateWorkspaceApiKeyResponse(BaseModel):
    keyName: StrictStr | None = None
    key: StrictStr | None = None
    workspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
