from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_ir import QuickSightTopicIR


class QuickSightTopicVisual(BaseModel):
    VisualId: StrictStr | None = None
    Role: StrictStr | None = None
    Ir: QuickSightTopicIR | None = None
    SupportingVisuals: list[QuickSightTopicVisual] | None = None
