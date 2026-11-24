from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .resilience_hub_resiliency_policy import ResilienceHubResiliencyPolicy


class ResilienceHubCreateResiliencyPolicyResponse(BaseModel):
    policy: ResilienceHubResiliencyPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
