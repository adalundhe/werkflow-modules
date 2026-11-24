from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_task_execution_list_entry import DataSyncTaskExecutionListEntry


class DataSyncListTaskExecutionsResponse(BaseModel):
    TaskExecutions: list[DataSyncTaskExecutionListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
