from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_workspace_theme import ConnectWorkspaceTheme


class ConnectUpdateWorkspaceThemeRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    Theme: ConnectWorkspaceTheme | None = None
