from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_slot import QuickSightSlot


class QuickSightTopicTemplate(BaseModel):
    TemplateType: StrictStr | None = None
    Slots: list[QuickSightSlot] | None = None
