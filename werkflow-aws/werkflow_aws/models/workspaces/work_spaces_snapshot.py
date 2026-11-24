from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesSnapshot(BaseModel):
    SnapshotTime: datetime.datetime | StrictStr | None = None
