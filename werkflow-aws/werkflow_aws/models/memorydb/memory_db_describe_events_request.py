from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeEventsRequest(BaseModel):
    SourceName: StrictStr | None = None
    SourceType: Literal['node', 'parameter-group', 'subnet-group', 'cluster', 'user', 'acl'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
