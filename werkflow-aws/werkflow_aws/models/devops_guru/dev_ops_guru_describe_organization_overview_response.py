from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class DevOpsGuruDescribeOrganizationOverviewResponse(BaseModel):
    ReactiveInsights: StrictInt | None = None
    ProactiveInsights: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
