from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruDescribeRecommendationFeedbackRequest(BaseModel):
    CodeReviewArn: StrictStr
    RecommendationId: StrictStr
    UserId: StrictStr | None = None
