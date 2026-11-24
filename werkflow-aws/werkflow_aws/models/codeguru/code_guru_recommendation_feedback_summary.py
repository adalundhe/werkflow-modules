from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruRecommendationFeedbackSummary(BaseModel):
    RecommendationId: StrictStr | None = None
    Reactions: list[StrictStr] | None = None
    UserId: StrictStr | None = None
