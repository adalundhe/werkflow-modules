import datetime
from pydantic import BaseModel, StrictStr, StrictInt
from .cloudwatch_metric_data_query import CloudWatchMetricDataQuery
from .cloudwatch_scan_by import CloudWatchScanBy
from .cloudwatch_label_options import CloudWatchLabelOptions

class CloudWatchGetMetricDataRequest(BaseModel):
    MetricDataQueries: list[CloudWatchMetricDataQuery]
    StartTime: datetime.datetime
    EndTime: datetime.datetime
    NextToken: StrictStr | None = None
    ScanBy: CloudWatchScanBy | None = None
    MaxDataPoints: StrictInt | None = None
    LabelOptions: CloudWatchLabelOptions | None = None