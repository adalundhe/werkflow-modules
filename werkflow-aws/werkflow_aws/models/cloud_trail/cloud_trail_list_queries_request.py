from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListQueriesRequest(BaseModel):
    EventDataStore: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    QueryStatus: Literal['QUEUED', 'RUNNING', 'FINISHED', 'FAILED', 'CANCELLED', 'TIMED_OUT'] | None = None
