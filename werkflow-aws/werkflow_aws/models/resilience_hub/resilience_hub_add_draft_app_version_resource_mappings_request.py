from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_resource_mapping import ResilienceHubResourceMapping


class ResilienceHubAddDraftAppVersionResourceMappingsRequest(BaseModel):
    appArn: StrictStr
    resourceMappings: list[ResilienceHubResourceMapping]
