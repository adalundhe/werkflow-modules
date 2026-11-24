from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction


class QuickSightEmptyVisual(BaseModel):
    VisualId: StrictStr | None = None
    DataSetIdentifier: StrictStr | None = None
    TopicIdentifier: StrictStr | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
