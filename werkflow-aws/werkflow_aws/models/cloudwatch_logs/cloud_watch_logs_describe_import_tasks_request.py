from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeImportTasksRequest(BaseModel):
    importId: StrictStr | None = None
    importStatus: Literal['IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED'] | None = None
    importSourceArn: StrictStr | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
