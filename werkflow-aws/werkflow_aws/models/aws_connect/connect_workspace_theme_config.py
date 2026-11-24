from __future__ import annotations
from pydantic import BaseModel
from .connect_workspace_theme_images import ConnectWorkspaceThemeImages
from .connect_workspace_theme_palette import ConnectWorkspaceThemePalette
from .connect_workspace_theme_typography import ConnectWorkspaceThemeTypography


class ConnectWorkspaceThemeConfig(BaseModel):
    Palette: ConnectWorkspaceThemePalette | None = None
    Images: ConnectWorkspaceThemeImages | None = None
    Typography: ConnectWorkspaceThemeTypography | None = None
