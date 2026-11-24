from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_component import ResilienceHubAppComponent


class ResilienceHubListAppVersionAppComponentsResponse(BaseModel):
    appArn: StrictStr | None = None
    appComponents: list[ResilienceHubAppComponent] | None = None
    appVersion: StrictStr | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
