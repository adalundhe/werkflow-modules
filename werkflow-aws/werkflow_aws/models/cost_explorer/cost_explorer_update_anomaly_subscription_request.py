from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_subscriber import CostExplorerSubscriber


class CostExplorerUpdateAnomalySubscriptionRequest(BaseModel):
    SubscriptionArn: StrictStr
    Threshold: StrictFloat | StrictInt | None = None
    Frequency: Literal['DAILY', 'IMMEDIATE', 'WEEKLY'] | None = None
    MonitorArnList: list[StrictStr] | None = None
    Subscribers: list[CostExplorerSubscriber] | None = None
    SubscriptionName: StrictStr | None = None
    ThresholdExpression: CostExplorerExpression | None = None
