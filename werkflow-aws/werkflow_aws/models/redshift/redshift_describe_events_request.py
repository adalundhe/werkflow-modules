from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeEventsRequest(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
