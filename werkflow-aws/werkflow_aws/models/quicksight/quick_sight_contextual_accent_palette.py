from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_palette import QuickSightPalette


class QuickSightContextualAccentPalette(BaseModel):
    Connection: QuickSightPalette | None = None
    Visualization: QuickSightPalette | None = None
    Insight: QuickSightPalette | None = None
    Automation: QuickSightPalette | None = None
