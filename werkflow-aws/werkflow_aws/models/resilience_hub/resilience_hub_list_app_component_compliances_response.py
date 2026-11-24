from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_component_compliance import ResilienceHubAppComponentCompliance


class ResilienceHubListAppComponentCompliancesResponse(BaseModel):
    componentCompliances: list[ResilienceHubAppComponentCompliance] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
