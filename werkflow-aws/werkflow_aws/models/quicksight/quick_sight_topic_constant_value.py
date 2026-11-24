from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_collective_constant_entry import QuickSightCollectiveConstantEntry


class QuickSightTopicConstantValue(BaseModel):
    ConstantType: StrictStr | None = None
    Value: StrictStr | None = None
    Minimum: StrictStr | None = None
    Maximum: StrictStr | None = None
    ValueList: list[QuickSightCollectiveConstantEntry] | None = None
