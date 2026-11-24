from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_click_feedback import KendraClickFeedback
from .kendra_relevance_feedback import KendraRelevanceFeedback


class KendraSubmitFeedbackRequest(BaseModel):
    IndexId: StrictStr
    QueryId: StrictStr
    ClickFeedbackItems: list[KendraClickFeedback] | None = None
    RelevanceFeedbackItems: list[KendraRelevanceFeedback] | None = None
