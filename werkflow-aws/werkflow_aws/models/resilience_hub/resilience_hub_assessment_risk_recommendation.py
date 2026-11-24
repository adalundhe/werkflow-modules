from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubAssessmentRiskRecommendation(BaseModel):
    appComponents: list[StrictStr] | None = None
    recommendation: StrictStr | None = None
    risk: StrictStr | None = None
