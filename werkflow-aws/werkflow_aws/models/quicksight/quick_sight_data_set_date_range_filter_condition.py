from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .quick_sight_data_set_date_filter_value import QuickSightDataSetDateFilterValue


class QuickSightDataSetDateRangeFilterCondition(BaseModel):
    RangeMinimum: QuickSightDataSetDateFilterValue | None = None
    RangeMaximum: QuickSightDataSetDateFilterValue | None = None
    IncludeMinimum: StrictBool | None = None
    IncludeMaximum: StrictBool | None = None
