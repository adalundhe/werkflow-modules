from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_gradient_stop import QuickSightGradientStop


class QuickSightGradientColor(BaseModel):
    Stops: list[QuickSightGradientStop] | None = None
