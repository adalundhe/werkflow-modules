from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_date_comparison_filter_condition import QuickSightDataSetDateComparisonFilterCondition
from .quick_sight_data_set_date_range_filter_condition import QuickSightDataSetDateRangeFilterCondition


class QuickSightDataSetDateFilterCondition(BaseModel):
    ColumnName: StrictStr | None = None
    ComparisonFilterCondition: QuickSightDataSetDateComparisonFilterCondition | None = None
    RangeFilterCondition: QuickSightDataSetDateRangeFilterCondition | None = None
