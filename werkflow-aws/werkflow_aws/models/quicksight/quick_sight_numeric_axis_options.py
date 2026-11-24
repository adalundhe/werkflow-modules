from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_range import QuickSightAxisDisplayRange
from .quick_sight_axis_scale import QuickSightAxisScale


class QuickSightNumericAxisOptions(BaseModel):
    Scale: QuickSightAxisScale | None = None
    Range: QuickSightAxisDisplayRange | None = None
