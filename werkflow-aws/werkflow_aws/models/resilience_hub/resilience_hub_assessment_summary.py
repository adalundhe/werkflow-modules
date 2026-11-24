from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_assessment_risk_recommendation import ResilienceHubAssessmentRiskRecommendation


class ResilienceHubAssessmentSummary(BaseModel):
    riskRecommendations: list[ResilienceHubAssessmentRiskRecommendation] | None = None
    summary: StrictStr | None = None
