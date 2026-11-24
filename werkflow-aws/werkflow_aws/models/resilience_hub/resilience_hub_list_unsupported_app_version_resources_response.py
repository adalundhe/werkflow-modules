from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_unsupported_resource import ResilienceHubUnsupportedResource


class ResilienceHubListUnsupportedAppVersionResourcesResponse(BaseModel):
    nextToken: StrictStr | None = None
    resolutionId: StrictStr | None = None
    unsupportedResources: list[ResilienceHubUnsupportedResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
