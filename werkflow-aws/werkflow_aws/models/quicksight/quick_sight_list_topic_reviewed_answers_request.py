from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListTopicReviewedAnswersRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
