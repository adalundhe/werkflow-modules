from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_string_list_filter_value import QuickSightDataSetStringListFilterValue


class QuickSightDataSetStringListFilterCondition(BaseModel):
    Operator: StrictStr | None = None
    Values: QuickSightDataSetStringListFilterValue | None = None
