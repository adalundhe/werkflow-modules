from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_topic_singular_filter_constant import QuickSightTopicSingularFilterConstant


class QuickSightTopicNullFilter(BaseModel):
    NullFilterType: StrictStr | None = None
    Constant: QuickSightTopicSingularFilterConstant | None = None
    Inverse: StrictBool | None = None
