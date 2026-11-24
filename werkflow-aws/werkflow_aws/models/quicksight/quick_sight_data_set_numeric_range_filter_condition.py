from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .quick_sight_data_set_numeric_filter_value import QuickSightDataSetNumericFilterValue


class QuickSightDataSetNumericRangeFilterCondition(BaseModel):
    RangeMinimum: QuickSightDataSetNumericFilterValue | None = None
    RangeMaximum: QuickSightDataSetNumericFilterValue | None = None
    IncludeMinimum: StrictBool | None = None
    IncludeMaximum: StrictBool | None = None
