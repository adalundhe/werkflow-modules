from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_resource_mapping import ResilienceHubResourceMapping


class ResilienceHubAddDraftAppVersionResourceMappingsResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    resourceMappings: list[ResilienceHubResourceMapping] | None = None
    ResponseMetadata: dict[str, Any] | None = None
