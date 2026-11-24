from __future__ import annotations
from pydantic import BaseModel
from .connect_workspace_theme_config import ConnectWorkspaceThemeConfig


class ConnectWorkspaceTheme(BaseModel):
    Light: ConnectWorkspaceThemeConfig | None = None
    Dark: ConnectWorkspaceThemeConfig | None = None
