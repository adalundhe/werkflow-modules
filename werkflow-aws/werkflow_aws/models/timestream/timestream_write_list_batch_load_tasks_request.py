from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamWriteListBatchLoadTasksRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    TaskStatus: Literal['CREATED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'PROGRESS_STOPPED', 'PENDING_RESUME'] | None = None
