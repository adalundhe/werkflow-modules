from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_version_summary import ResilienceHubAppVersionSummary


class ResilienceHubListAppVersionsResponse(BaseModel):
    appVersions: list[ResilienceHubAppVersionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
