from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_date_filter_value import QuickSightDataSetDateFilterValue


class QuickSightDataSetDateComparisonFilterCondition(BaseModel):
    Operator: StrictStr | None = None
    Value: QuickSightDataSetDateFilterValue | None = None
