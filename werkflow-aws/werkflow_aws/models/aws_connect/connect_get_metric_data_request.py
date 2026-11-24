from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_filters import ConnectFilters
from .connect_historical_metric import ConnectHistoricalMetric


class ConnectGetMetricDataRequest(BaseModel):
    InstanceId: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Filters: ConnectFilters
    HistoricalMetrics: list[ConnectHistoricalMetric]
    Groupings: list[Literal['QUEUE', 'CHANNEL', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION', 'AGENT_STATUS', 'SUBTYPE', 'VALIDATION_TEST_TYPE']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
