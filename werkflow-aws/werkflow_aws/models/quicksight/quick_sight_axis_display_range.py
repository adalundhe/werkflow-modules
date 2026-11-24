from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_data_driven_range import QuickSightAxisDisplayDataDrivenRange
from .quick_sight_axis_display_min_max_range import QuickSightAxisDisplayMinMaxRange


class QuickSightAxisDisplayRange(BaseModel):
    MinMax: QuickSightAxisDisplayMinMaxRange | None = None
    DataDriven: QuickSightAxisDisplayDataDrivenRange | None = None
