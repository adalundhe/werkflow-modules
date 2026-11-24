from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_task_list_entry import DataSyncTaskListEntry


class DataSyncListTasksResponse(BaseModel):
    Tasks: list[DataSyncTaskListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
