from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_import import CloudWatchLogsImport


class CloudWatchLogsDescribeImportTasksResponse(BaseModel):
    imports: list[CloudWatchLogsImport] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
