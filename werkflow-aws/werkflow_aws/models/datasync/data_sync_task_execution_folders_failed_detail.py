from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataSyncTaskExecutionFoldersFailedDetail(BaseModel):
    List: StrictInt | None = None
    Prepare: StrictInt | None = None
    Transfer: StrictInt | None = None
    Verify: StrictInt | None = None
    Delete: StrictInt | None = None
