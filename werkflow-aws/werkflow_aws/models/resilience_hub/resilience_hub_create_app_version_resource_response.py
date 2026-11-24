from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_physical_resource import ResilienceHubPhysicalResource


class ResilienceHubCreateAppVersionResourceResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    physicalResource: ResilienceHubPhysicalResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
