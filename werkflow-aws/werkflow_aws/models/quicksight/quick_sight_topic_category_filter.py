from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_topic_category_filter_constant import QuickSightTopicCategoryFilterConstant


class QuickSightTopicCategoryFilter(BaseModel):
    CategoryFilterFunction: StrictStr | None = None
    CategoryFilterType: StrictStr | None = None
    Constant: QuickSightTopicCategoryFilterConstant | None = None
    Inverse: StrictBool | None = None
    NullFilter: StrictStr | None = None
