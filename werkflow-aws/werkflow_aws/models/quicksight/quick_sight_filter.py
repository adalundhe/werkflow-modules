from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_category_filter import QuickSightCategoryFilter
from .quick_sight_hierarchy_filter import QuickSightHierarchyFilter
from .quick_sight_nested_filter import QuickSightNestedFilter
from .quick_sight_numeric_equality_filter import QuickSightNumericEqualityFilter
from .quick_sight_numeric_range_filter import QuickSightNumericRangeFilter
from .quick_sight_relative_dates_filter import QuickSightRelativeDatesFilter
from .quick_sight_time_equality_filter import QuickSightTimeEqualityFilter
from .quick_sight_time_range_filter import QuickSightTimeRangeFilter
from .quick_sight_top_bottom_filter import QuickSightTopBottomFilter


class QuickSightFilter(BaseModel):
    CategoryFilter: QuickSightCategoryFilter | None = None
    NumericRangeFilter: QuickSightNumericRangeFilter | None = None
    NumericEqualityFilter: QuickSightNumericEqualityFilter | None = None
    TimeEqualityFilter: QuickSightTimeEqualityFilter | None = None
    TimeRangeFilter: QuickSightTimeRangeFilter | None = None
    RelativeDatesFilter: QuickSightRelativeDatesFilter | None = None
    TopBottomFilter: QuickSightTopBottomFilter | None = None
    NestedFilter: QuickSightNestedFilter | None = None
    HierarchyFilter: QuickSightHierarchyFilter | None = None
