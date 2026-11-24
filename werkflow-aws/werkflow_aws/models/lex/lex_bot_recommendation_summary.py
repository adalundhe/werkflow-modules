from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotRecommendationSummary(BaseModel):
    botRecommendationStatus: StrictStr | None = None
    botRecommendationId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
