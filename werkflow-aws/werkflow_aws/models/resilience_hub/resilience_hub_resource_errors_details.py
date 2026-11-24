from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .resilience_hub_resource_error import ResilienceHubResourceError


class ResilienceHubResourceErrorsDetails(BaseModel):
    hasMoreErrors: StrictBool | None = None
    resourceErrors: list[ResilienceHubResourceError] | None = None
