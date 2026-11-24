from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_workspace_theme import ConnectWorkspaceTheme


class ConnectCreateWorkspaceRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Description: StrictStr | None = None
    Theme: ConnectWorkspaceTheme | None = None
    Title: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
