from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_metric_search_criteria import ConnectMetricSearchCriteria
from .connect_metric_search_filter import ConnectMetricSearchFilter


class ConnectSearchMetricsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectMetricSearchFilter | None = None
    SearchCriteria: ConnectMetricSearchCriteria | None = None
