from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_border_style import QuickSightBorderStyle


class QuickSightTileStyle(BaseModel):
    BackgroundColor: StrictStr | None = None
    Border: QuickSightBorderStyle | None = None
    BorderRadius: StrictStr | None = None
    Padding: StrictStr | None = None
