from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeEventsRequest(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: Literal['db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot', 'db-cluster', 'db-cluster-snapshot'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    EventCategories: list[StrictStr] | None = None
    Filters: list[NeptuneFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
