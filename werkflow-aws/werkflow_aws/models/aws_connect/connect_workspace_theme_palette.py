from __future__ import annotations
from pydantic import BaseModel
from .connect_palette_canvas import ConnectPaletteCanvas
from .connect_palette_header import ConnectPaletteHeader
from .connect_palette_navigation import ConnectPaletteNavigation
from .connect_palette_primary import ConnectPalettePrimary


class ConnectWorkspaceThemePalette(BaseModel):
    Header: ConnectPaletteHeader | None = None
    Navigation: ConnectPaletteNavigation | None = None
    Canvas: ConnectPaletteCanvas | None = None
    Primary: ConnectPalettePrimary | None = None
