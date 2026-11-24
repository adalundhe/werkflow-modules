from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_palette import QuickSightPalette


class QuickSightBrandColorPalette(BaseModel):
    Primary: QuickSightPalette | None = None
    Secondary: QuickSightPalette | None = None
    Accent: QuickSightPalette | None = None
    Measure: QuickSightPalette | None = None
    Dimension: QuickSightPalette | None = None
    Success: QuickSightPalette | None = None
    Info: QuickSightPalette | None = None
    Warning: QuickSightPalette | None = None
    Danger: QuickSightPalette | None = None
