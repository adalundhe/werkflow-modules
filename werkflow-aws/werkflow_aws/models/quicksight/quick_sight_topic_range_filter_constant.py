from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_range_constant import QuickSightRangeConstant


class QuickSightTopicRangeFilterConstant(BaseModel):
    ConstantType: StrictStr | None = None
    RangeConstant: QuickSightRangeConstant | None = None
