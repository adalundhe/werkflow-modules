from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataSyncTaskExecutionFilesListedDetail(BaseModel):
    AtSource: StrictInt | None = None
    AtDestinationForDelete: StrictInt | None = None
