from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_metric_stat_model import CloudWatchMetricStatModel


class CloudWatchMetricDataQueryModel(BaseModel):
    Id: StrictStr | None = None
    MetricStat: CloudWatchMetricStatModel | None = None
    Expression: StrictStr | None = None
    Label: StrictStr | None = None
    ReturnData: StrictBool | None = None
    Period: StrictInt | None = None
    AccountId: StrictStr | None = None
