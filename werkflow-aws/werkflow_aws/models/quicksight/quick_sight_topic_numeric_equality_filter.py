from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_topic_singular_filter_constant import QuickSightTopicSingularFilterConstant


class QuickSightTopicNumericEqualityFilter(BaseModel):
    Constant: QuickSightTopicSingularFilterConstant | None = None
    Aggregation: StrictStr | None = None
    Inverse: StrictBool | None = None
    NullFilter: StrictStr | None = None
