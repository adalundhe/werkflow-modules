from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupCalculatedLifecycle(BaseModel):
    MoveToColdStorageAt: datetime.datetime | StrictStr | None = None
    DeleteAt: datetime.datetime | StrictStr | None = None
