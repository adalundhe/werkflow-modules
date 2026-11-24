from __future__ import annotations
from pydantic import BaseModel
from .connect_font_family import ConnectFontFamily


class ConnectWorkspaceThemeTypography(BaseModel):
    FontFamily: ConnectFontFamily | None = None
