from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_write_batch_load_task import TimestreamWriteBatchLoadTask


class TimestreamWriteListBatchLoadTasksResponse(BaseModel):
    NextToken: StrictStr | None = None
    BatchLoadTasks: list[TimestreamWriteBatchLoadTask] | None = None
    ResponseMetadata: dict[str, Any] | None = None
