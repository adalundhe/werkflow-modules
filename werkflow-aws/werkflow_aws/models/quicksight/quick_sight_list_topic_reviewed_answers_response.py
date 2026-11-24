from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_reviewed_answer import QuickSightTopicReviewedAnswer


class QuickSightListTopicReviewedAnswersResponse(BaseModel):
    TopicId: StrictStr | None = None
    TopicArn: StrictStr | None = None
    Answers: list[QuickSightTopicReviewedAnswer] | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
