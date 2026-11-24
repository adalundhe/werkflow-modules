from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailQueryStatisticsForDescribeQuery(BaseModel):
    EventsMatched: StrictInt | None = None
    EventsScanned: StrictInt | None = None
    BytesScanned: StrictInt | None = None
    ExecutionTimeInMillis: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
