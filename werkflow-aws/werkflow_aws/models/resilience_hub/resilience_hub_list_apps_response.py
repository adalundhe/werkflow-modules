from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_summary import ResilienceHubAppSummary


class ResilienceHubListAppsResponse(BaseModel):
    appSummaries: list[ResilienceHubAppSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
