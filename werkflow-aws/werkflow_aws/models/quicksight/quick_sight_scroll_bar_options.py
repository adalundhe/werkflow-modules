from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_visible_range_options import QuickSightVisibleRangeOptions


class QuickSightScrollBarOptions(BaseModel):
    Visibility: StrictStr | None = None
    VisibleRange: QuickSightVisibleRangeOptions | None = None
