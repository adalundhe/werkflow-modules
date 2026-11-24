from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_insight_feedback_entity import OpenSearchInsightFeedbackEntity


class OpenSearchInsightFeedbackRequest(BaseModel):
    Entity: OpenSearchInsightFeedbackEntity
    InsightId: StrictStr
    Thumbs: Literal['Up', 'Down']
    FeedbackText: StrictStr | None = None
