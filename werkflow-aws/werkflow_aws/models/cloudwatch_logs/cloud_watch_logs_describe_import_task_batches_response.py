from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_import_batch import CloudWatchLogsImportBatch


class CloudWatchLogsDescribeImportTaskBatchesResponse(BaseModel):
    importSourceArn: StrictStr | None = None
    importId: StrictStr | None = None
    importBatches: list[CloudWatchLogsImportBatch] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
