from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_sync_task_filter import DataSyncTaskFilter


class DataSyncListTasksRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[DataSyncTaskFilter] | None = None
