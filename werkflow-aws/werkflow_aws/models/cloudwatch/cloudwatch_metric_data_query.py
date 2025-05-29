from pydantic import BaseModel, StrictStr, StrictBool, StrictInt
from .cloudwatch_metric_stat import CloudWatchMetricStat

class CloudWatchMetricDataQuery(BaseModel):
    Id: StrictStr
    MetricStat: CloudWatchMetricStat
    Expression: StrictStr | None = None
    Label: StrictStr | None = None
    ReturnData: StrictBool = False
    Period: StrictInt | None = None
    AccountId: StrictStr | None = None