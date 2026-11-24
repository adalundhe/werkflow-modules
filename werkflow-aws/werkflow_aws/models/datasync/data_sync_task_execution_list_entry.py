from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncTaskExecutionListEntry(BaseModel):
    TaskExecutionArn: StrictStr | None = None
    Status: StrictStr | None = None
    TaskMode: StrictStr | None = None
