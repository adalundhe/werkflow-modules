from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubRecommendationDisruptionCompliance(BaseModel):
    expectedComplianceStatus: StrictStr | None = None
    expectedRpoDescription: StrictStr | None = None
    expectedRpoInSecs: StrictInt | None = None
    expectedRtoDescription: StrictStr | None = None
    expectedRtoInSecs: StrictInt | None = None
