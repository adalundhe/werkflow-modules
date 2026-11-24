from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDeleteTopicReviewedAnswerRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    AnswerIds: list[StrictStr] | None = None
