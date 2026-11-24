from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_assessment_summary import ResilienceHubAppAssessmentSummary


class ResilienceHubListAppAssessmentsResponse(BaseModel):
    assessmentSummaries: list[ResilienceHubAppAssessmentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
