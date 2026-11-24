from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_resources_trends_metrics_result import SecurityHubResourcesTrendsMetricsResult


class SecurityHubGetResourcesTrendsV2Response(BaseModel):
    Granularity: StrictStr | None = None
    TrendsMetrics: list[SecurityHubResourcesTrendsMetricsResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
