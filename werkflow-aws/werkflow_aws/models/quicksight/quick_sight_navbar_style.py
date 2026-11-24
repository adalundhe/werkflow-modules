from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_palette import QuickSightPalette


class QuickSightNavbarStyle(BaseModel):
    GlobalNavbar: QuickSightPalette | None = None
    ContextualNavbar: QuickSightPalette | None = None
