from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubBatchUpdateRecommendationStatusFailedEntry(BaseModel):
    entryId: StrictStr | None = None
    errorMessage: StrictStr | None = None
