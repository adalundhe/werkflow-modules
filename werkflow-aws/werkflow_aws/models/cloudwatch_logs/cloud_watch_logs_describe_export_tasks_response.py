from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_export_task import CloudWatchLogsExportTask


class CloudWatchLogsDescribeExportTasksResponse(BaseModel):
    exportTasks: list[CloudWatchLogsExportTask] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
