from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_physical_resource import ResilienceHubPhysicalResource


class ResilienceHubListAppVersionResourcesResponse(BaseModel):
    nextToken: StrictStr | None = None
    physicalResources: list[ResilienceHubPhysicalResource] | None = None
    resolutionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
