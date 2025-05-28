from pydantic import BaseModel, StrictStr
from .cloudwatch_metric import CloudWatchMetric


class CloudWatchListMetricsResponse(BaseModel):
    Metrics: list[CloudWatchMetric]
    NextToken: StrictStr | None = None
    OwningAccounts: list[StrictStr] | None = None