from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_axis_options import QuickSightDateAxisOptions
from .quick_sight_numeric_axis_options import QuickSightNumericAxisOptions


class QuickSightAxisDataOptions(BaseModel):
    NumericAxisOptions: QuickSightNumericAxisOptions | None = None
    DateAxisOptions: QuickSightDateAxisOptions | None = None
