import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .cloudwatch_label_options import CloudWatchLabelOptions
from .cloudwatch_metric_data_query import CloudWatchMetricDataQuery
from .cloudwatch_scan_by import CloudWatchScanBy


class CloudWatchGetMetricDataRequest(BaseModel):
    MetricDataQueries: list[CloudWatchMetricDataQuery]
    StartTime: datetime.datetime
    EndTime: datetime.datetime
    NextToken: StrictStr | None = None
    ScanBy: CloudWatchScanBy | None = None
    MaxDatapoints: StrictInt | None = None
    LabelOptions: CloudWatchLabelOptions | None = None
