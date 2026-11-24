from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_topic_range_filter_constant import QuickSightTopicRangeFilterConstant


class QuickSightTopicNumericRangeFilter(BaseModel):
    Inclusive: StrictBool | None = None
    Constant: QuickSightTopicRangeFilterConstant | None = None
    Aggregation: StrictStr | None = None
    Inverse: StrictBool | None = None
    NullFilter: StrictStr | None = None
