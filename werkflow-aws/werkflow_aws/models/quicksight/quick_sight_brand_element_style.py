from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_navbar_style import QuickSightNavbarStyle


class QuickSightBrandElementStyle(BaseModel):
    NavbarStyle: QuickSightNavbarStyle | None = None
