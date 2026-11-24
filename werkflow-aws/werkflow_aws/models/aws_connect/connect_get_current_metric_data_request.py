from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_current_metric import ConnectCurrentMetric
from .connect_current_metric_sort_criteria import ConnectCurrentMetricSortCriteria
from .connect_filters import ConnectFilters


class ConnectGetCurrentMetricDataRequest(BaseModel):
    InstanceId: StrictStr
    Filters: ConnectFilters
    CurrentMetrics: list[ConnectCurrentMetric]
    Groupings: list[Literal['QUEUE', 'CHANNEL', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION', 'AGENT_STATUS', 'SUBTYPE', 'VALIDATION_TEST_TYPE']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortCriteria: list[ConnectCurrentMetricSortCriteria] | None = None
