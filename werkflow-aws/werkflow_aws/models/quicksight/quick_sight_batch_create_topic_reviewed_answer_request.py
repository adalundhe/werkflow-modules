from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_create_topic_reviewed_answer import QuickSightCreateTopicReviewedAnswer


class QuickSightBatchCreateTopicReviewedAnswerRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    Answers: list[QuickSightCreateTopicReviewedAnswer]
