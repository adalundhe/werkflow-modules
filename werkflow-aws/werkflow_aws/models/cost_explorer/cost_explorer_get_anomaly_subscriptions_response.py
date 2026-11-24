from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_anomaly_subscription import CostExplorerAnomalySubscription


class CostExplorerGetAnomalySubscriptionsResponse(BaseModel):
    AnomalySubscriptions: list[CostExplorerAnomalySubscription] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
