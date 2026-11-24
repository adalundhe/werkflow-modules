from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeGuruPutRecommendationFeedbackRequest(BaseModel):
    CodeReviewArn: StrictStr
    RecommendationId: StrictStr
    Reactions: list[Literal['ThumbsUp', 'ThumbsDown']]
