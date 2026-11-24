from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_string_comparison_filter_condition import QuickSightDataSetStringComparisonFilterCondition
from .quick_sight_data_set_string_list_filter_condition import QuickSightDataSetStringListFilterCondition


class QuickSightDataSetStringFilterCondition(BaseModel):
    ColumnName: StrictStr | None = None
    ComparisonFilterCondition: QuickSightDataSetStringComparisonFilterCondition | None = None
    ListFilterCondition: QuickSightDataSetStringListFilterCondition | None = None
