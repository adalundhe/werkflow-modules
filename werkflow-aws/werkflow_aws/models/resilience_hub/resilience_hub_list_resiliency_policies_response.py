from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_resiliency_policy import ResilienceHubResiliencyPolicy


class ResilienceHubListResiliencyPoliciesResponse(BaseModel):
    nextToken: StrictStr | None = None
    resiliencyPolicies: list[ResilienceHubResiliencyPolicy] | None = None
    ResponseMetadata: dict[str, Any] | None = None
