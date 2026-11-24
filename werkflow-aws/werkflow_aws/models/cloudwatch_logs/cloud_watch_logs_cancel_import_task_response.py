from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_import_statistics import CloudWatchLogsImportStatistics


class CloudWatchLogsCancelImportTaskResponse(BaseModel):
    importId: StrictStr | None = None
    importStatistics: CloudWatchLogsImportStatistics | None = None
    importStatus: StrictStr | None = None
    creationTime: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
