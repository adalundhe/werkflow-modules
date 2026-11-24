from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_category_drill_down_filter import QuickSightCategoryDrillDownFilter
from .quick_sight_numeric_equality_drill_down_filter import QuickSightNumericEqualityDrillDownFilter
from .quick_sight_time_range_drill_down_filter import QuickSightTimeRangeDrillDownFilter


class QuickSightDrillDownFilter(BaseModel):
    NumericEqualityFilter: QuickSightNumericEqualityDrillDownFilter | None = None
    CategoryFilter: QuickSightCategoryDrillDownFilter | None = None
    TimeRangeFilter: QuickSightTimeRangeDrillDownFilter | None = None
