from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_resource_drift import ResilienceHubResourceDrift


class ResilienceHubListAppAssessmentResourceDriftsResponse(BaseModel):
    nextToken: StrictStr | None = None
    resourceDrifts: list[ResilienceHubResourceDrift] | None = None
    ResponseMetadata: dict[str, Any] | None = None
