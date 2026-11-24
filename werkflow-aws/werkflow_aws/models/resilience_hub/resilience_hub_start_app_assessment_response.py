from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .resilience_hub_app_assessment import ResilienceHubAppAssessment


class ResilienceHubStartAppAssessmentResponse(BaseModel):
    assessment: ResilienceHubAppAssessment | None = None
    ResponseMetadata: dict[str, Any] | None = None
