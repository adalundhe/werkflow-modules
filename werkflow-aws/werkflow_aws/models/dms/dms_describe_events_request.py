from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeEventsRequest(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: Literal['replication-instance'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    EventCategories: list[StrictStr] | None = None
    Filters: list[DMSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
