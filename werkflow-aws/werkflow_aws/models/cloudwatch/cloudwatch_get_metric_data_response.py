from pydantic import BaseModel, StrictStr
from .cloudwatch_metric_data_result import CloudWatchMetricDataResult
from .cloudwatch_message import CloudWatchMessage

class CloudWatchGetMetricDataResponse(BaseModel):
    MetricDataResults: list[CloudWatchMetricDataResult]
    NextToken: StrictStr | None = None
    Messages: list[CloudWatchMessage] | None = None