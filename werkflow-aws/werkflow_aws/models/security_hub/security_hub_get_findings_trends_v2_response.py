from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_trends_metrics_result import SecurityHubTrendsMetricsResult


class SecurityHubGetFindingsTrendsV2Response(BaseModel):
    Granularity: StrictStr | None = None
    TrendsMetrics: list[SecurityHubTrendsMetricsResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
