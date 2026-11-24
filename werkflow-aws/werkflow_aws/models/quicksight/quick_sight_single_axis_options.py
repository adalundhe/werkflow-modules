from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_y_axis_options import QuickSightYAxisOptions


class QuickSightSingleAxisOptions(BaseModel):
    YAxisOptions: QuickSightYAxisOptions | None = None
