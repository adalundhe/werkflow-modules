from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class DevOpsGuruDescribeOrganizationHealthResponse(BaseModel):
    OpenReactiveInsights: StrictInt | None = None
    OpenProactiveInsights: StrictInt | None = None
    MetricsAnalyzed: StrictInt | None = None
    ResourceHours: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
