from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncTaskListEntry(BaseModel):
    TaskArn: StrictStr | None = None
    Status: StrictStr | None = None
    Name: StrictStr | None = None
    TaskMode: StrictStr | None = None
