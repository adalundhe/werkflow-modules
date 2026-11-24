from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_percent_visible_range import QuickSightPercentVisibleRange


class QuickSightVisibleRangeOptions(BaseModel):
    PercentRange: QuickSightPercentVisibleRange | None = None
