from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TimestreamWriteBatchLoadTask(BaseModel):
    TaskId: StrictStr | None = None
    TaskStatus: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ResumableUntil: datetime.datetime | StrictStr | None = None
