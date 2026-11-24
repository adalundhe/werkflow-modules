from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_insight_results import SecurityHubInsightResults


class SecurityHubGetInsightResultsResponse(BaseModel):
    InsightResults: SecurityHubInsightResults | None = None
    ResponseMetadata: dict[str, Any] | None = None
