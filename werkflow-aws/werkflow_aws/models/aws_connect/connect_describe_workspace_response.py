from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_workspace import ConnectWorkspace


class ConnectDescribeWorkspaceResponse(BaseModel):
    Workspace: ConnectWorkspace | None = None
    ResponseMetadata: dict[str, Any] | None = None
