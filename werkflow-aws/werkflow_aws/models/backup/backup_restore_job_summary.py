from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupRestoreJobSummary(BaseModel):
    Region: StrictStr | None = None
    AccountId: StrictStr | None = None
    State: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Count: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
