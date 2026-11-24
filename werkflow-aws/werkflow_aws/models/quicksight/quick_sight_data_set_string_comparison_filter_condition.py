from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_string_filter_value import QuickSightDataSetStringFilterValue


class QuickSightDataSetStringComparisonFilterCondition(BaseModel):
    Operator: StrictStr | None = None
    Value: QuickSightDataSetStringFilterValue | None = None
