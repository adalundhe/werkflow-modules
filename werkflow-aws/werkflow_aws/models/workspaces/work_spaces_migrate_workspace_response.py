from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkSpacesMigrateWorkspaceResponse(BaseModel):
    SourceWorkspaceId: StrictStr | None = None
    TargetWorkspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
