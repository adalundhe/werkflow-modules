from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_singular_filter_constant import QuickSightTopicSingularFilterConstant


class QuickSightTopicRelativeDateFilter(BaseModel):
    TimeGranularity: StrictStr | None = None
    RelativeDateFilterFunction: StrictStr | None = None
    Constant: QuickSightTopicSingularFilterConstant | None = None
    NullFilter: StrictStr | None = None
