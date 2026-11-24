from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_topic_range_filter_constant import QuickSightTopicRangeFilterConstant


class QuickSightTopicDateRangeFilter(BaseModel):
    Inclusive: StrictBool | None = None
    Constant: QuickSightTopicRangeFilterConstant | None = None
    NullFilter: StrictStr | None = None
