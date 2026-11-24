from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_import_filter import CloudWatchLogsImportFilter


class CloudWatchLogsCreateImportTaskRequest(BaseModel):
    importSourceArn: StrictStr
    importRoleArn: StrictStr
    importFilter: CloudWatchLogsImportFilter | None = None
