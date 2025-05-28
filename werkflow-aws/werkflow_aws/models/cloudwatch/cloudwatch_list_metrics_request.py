from typing import Literal
from pydantic import BaseModel, StrictStr, StrictBool
from .cloudwatch_dimension import CloudWatchDimension


class CloudWatchListMetricsRequest(BaseModel):
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimension] | None = None
    NextToken: StrictStr | None = None
    RecentlyActive: Literal["PT3H"] | None = None
    IncludeLinkedAccounts: StrictBool = False
    OwningAccount: StrictStr | None = None