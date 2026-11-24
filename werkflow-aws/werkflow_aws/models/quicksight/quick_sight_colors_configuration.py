from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_color import QuickSightCustomColor


class QuickSightColorsConfiguration(BaseModel):
    CustomColors: list[QuickSightCustomColor] | None = None
