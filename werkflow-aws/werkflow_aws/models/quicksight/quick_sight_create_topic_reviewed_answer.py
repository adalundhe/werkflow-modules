from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_ir import QuickSightTopicIR
from .quick_sight_topic_template import QuickSightTopicTemplate
from .quick_sight_topic_visual import QuickSightTopicVisual


class QuickSightCreateTopicReviewedAnswer(BaseModel):
    AnswerId: StrictStr
    DatasetArn: StrictStr
    Question: StrictStr
    Mir: QuickSightTopicIR | None = None
    PrimaryVisual: QuickSightTopicVisual | None = None
    Template: QuickSightTopicTemplate | None = None
