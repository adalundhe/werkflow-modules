from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_batch_load_task_description import TimestreamWriteBatchLoadTaskDescription


class TimestreamWriteDescribeBatchLoadTaskResponse(BaseModel):
    BatchLoadTaskDescription: TimestreamWriteBatchLoadTaskDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
