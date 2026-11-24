from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_numeric_filter_value import QuickSightDataSetNumericFilterValue


class QuickSightDataSetNumericComparisonFilterCondition(BaseModel):
    Operator: StrictStr | None = None
    Value: QuickSightDataSetNumericFilterValue | None = None
