from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateWorkspaceResponse(BaseModel):
    WorkspaceId: StrictStr | None = None
    WorkspaceArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
