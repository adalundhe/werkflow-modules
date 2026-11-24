from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_invalid_topic_reviewed_answer import QuickSightInvalidTopicReviewedAnswer
from .quick_sight_succeeded_topic_reviewed_answer import QuickSightSucceededTopicReviewedAnswer


class QuickSightBatchDeleteTopicReviewedAnswerResponse(BaseModel):
    TopicId: StrictStr | None = None
    TopicArn: StrictStr | None = None
    SucceededAnswers: list[QuickSightSucceededTopicReviewedAnswer] | None = None
    InvalidAnswers: list[QuickSightInvalidTopicReviewedAnswer] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
