from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeGuruListRecommendationFeedbackRequest(BaseModel):
    CodeReviewArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    UserIds: list[StrictStr] | None = None
    RecommendationIds: list[StrictStr] | None = None
