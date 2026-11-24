from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerGetAnomalySubscriptionsRequest(BaseModel):
    SubscriptionArnList: list[StrictStr] | None = None
    MonitorArn: StrictStr | None = None
    NextPageToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
