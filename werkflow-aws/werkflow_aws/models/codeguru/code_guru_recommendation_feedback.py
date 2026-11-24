from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeGuruRecommendationFeedback(BaseModel):
    CodeReviewArn: StrictStr | None = None
    RecommendationId: StrictStr | None = None
    Reactions: list[StrictStr] | None = None
    UserId: StrictStr | None = None
    CreatedTimeStamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimeStamp: datetime.datetime | StrictStr | None = None
