from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_date_filter_condition import QuickSightDataSetDateFilterCondition
from .quick_sight_data_set_numeric_filter_condition import QuickSightDataSetNumericFilterCondition
from .quick_sight_data_set_string_filter_condition import QuickSightDataSetStringFilterCondition


class QuickSightFilterOperation(BaseModel):
    ConditionExpression: StrictStr | None = None
    StringFilterCondition: QuickSightDataSetStringFilterCondition | None = None
    NumericFilterCondition: QuickSightDataSetNumericFilterCondition | None = None
    DateFilterCondition: QuickSightDataSetDateFilterCondition | None = None
