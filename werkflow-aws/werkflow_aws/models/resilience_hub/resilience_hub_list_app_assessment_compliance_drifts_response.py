from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_compliance_drift import ResilienceHubComplianceDrift


class ResilienceHubListAppAssessmentComplianceDriftsResponse(BaseModel):
    complianceDrifts: list[ResilienceHubComplianceDrift] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
