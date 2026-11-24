from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_numeric_comparison_filter_condition import QuickSightDataSetNumericComparisonFilterCondition
from .quick_sight_data_set_numeric_range_filter_condition import QuickSightDataSetNumericRangeFilterCondition


class QuickSightDataSetNumericFilterCondition(BaseModel):
    ColumnName: StrictStr | None = None
    ComparisonFilterCondition: QuickSightDataSetNumericComparisonFilterCondition | None = None
    RangeFilterCondition: QuickSightDataSetNumericRangeFilterCondition | None = None
