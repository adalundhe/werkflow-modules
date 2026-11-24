from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_filter_v2 import ConnectFilterV2
from .connect_interval_details import ConnectIntervalDetails
from .connect_metric_v2 import ConnectMetricV2


class ConnectGetMetricDataV2Request(BaseModel):
    ResourceArn: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Filters: list[ConnectFilterV2]
    Metrics: list[ConnectMetricV2]
    Interval: ConnectIntervalDetails | None = None
    Groupings: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
