from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_subscriber import CostExplorerSubscriber


class CostExplorerAnomalySubscription(BaseModel):
    SubscriptionArn: StrictStr | None = None
    AccountId: StrictStr | None = None
    MonitorArnList: list[StrictStr] | None = None
    Subscribers: list[CostExplorerSubscriber] | None = None
    Threshold: StrictFloat | StrictInt | None = None
    Frequency: StrictStr | None = None
    SubscriptionName: StrictStr | None = None
    ThresholdExpression: CostExplorerExpression | None = None
