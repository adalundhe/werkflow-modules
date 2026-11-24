from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_collective_constant import QuickSightCollectiveConstant


class QuickSightTopicCategoryFilterConstant(BaseModel):
    ConstantType: StrictStr | None = None
    SingularConstant: StrictStr | None = None
    CollectiveConstant: QuickSightCollectiveConstant | None = None
