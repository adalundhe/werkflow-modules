from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_anomaly_subscription import CostExplorerAnomalySubscription
from .cost_explorer_resource_tag import CostExplorerResourceTag


class CostExplorerCreateAnomalySubscriptionRequest(BaseModel):
    AnomalySubscription: CostExplorerAnomalySubscription
    ResourceTags: list[CostExplorerResourceTag] | None = None
