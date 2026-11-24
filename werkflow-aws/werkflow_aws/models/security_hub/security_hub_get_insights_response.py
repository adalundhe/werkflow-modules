from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_insight import SecurityHubInsight


class SecurityHubGetInsightsResponse(BaseModel):
    Insights: list[SecurityHubInsight] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
