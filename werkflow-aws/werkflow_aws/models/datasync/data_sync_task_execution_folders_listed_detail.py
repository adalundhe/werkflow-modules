from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataSyncTaskExecutionFoldersListedDetail(BaseModel):
    AtSource: StrictInt | None = None
    AtDestinationForDelete: StrictInt | None = None
