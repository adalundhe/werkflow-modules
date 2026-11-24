from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class DevOpsGuruDescribeAccountOverviewResponse(BaseModel):
    ReactiveInsights: StrictInt | None = None
    ProactiveInsights: StrictInt | None = None
    MeanTimeToRecoverInMilliseconds: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
