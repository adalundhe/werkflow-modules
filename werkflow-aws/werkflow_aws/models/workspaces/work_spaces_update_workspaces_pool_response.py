from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .workspaces_pool import WorkspacesPool as _WorkspacesPoolType


class WorkSpacesUpdateWorkspacesPoolResponse(BaseModel):
    WorkspacesPool: _WorkspacesPoolType | None = None
    ResponseMetadata: dict[str, Any] | None = None
