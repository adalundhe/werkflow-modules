from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeExportTasksRequest(BaseModel):
    taskId: StrictStr | None = None
    statusCode: Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING'] | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
