from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceSnapshot(BaseModel):
    DirectoryId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
