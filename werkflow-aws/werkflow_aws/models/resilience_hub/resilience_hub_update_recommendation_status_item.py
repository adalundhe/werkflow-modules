from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubUpdateRecommendationStatusItem(BaseModel):
    resourceId: StrictStr | None = None
    targetAccountId: StrictStr | None = None
    targetRegion: StrictStr | None = None
