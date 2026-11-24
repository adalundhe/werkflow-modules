from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeEventsRequest(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
