from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeImportTaskBatchesRequest(BaseModel):
    importId: StrictStr
    batchImportStatus: list[Literal['IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED']] | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
