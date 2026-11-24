from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDeleteWorkspaceServiceAccountResponse(BaseModel):
    serviceAccountId: StrictStr | None = None
    workspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
