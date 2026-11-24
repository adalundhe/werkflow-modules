from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class FSxDataRepositoryTaskStatus(BaseModel):
    TotalCount: StrictInt | None = None
    SucceededCount: StrictInt | None = None
    FailedCount: StrictInt | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ReleasedCapacity: StrictInt | None = None
