from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from .cloud_watch_logs_export_task_execution_info import CloudWatchLogsExportTaskExecutionInfo
from .cloud_watch_logs_export_task_status import CloudWatchLogsExportTaskStatus


class CloudWatchLogsExportTask(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    taskId: StrictStr | None = None
    taskName: StrictStr | None = None
    logGroupName: StrictStr | None = None
    from_: StrictInt | None = Field(default=None, alias='from')
    to: StrictInt | None = None
    destination: StrictStr | None = None
    destinationPrefix: StrictStr | None = None
    status: CloudWatchLogsExportTaskStatus | None = None
    executionInfo: CloudWatchLogsExportTaskExecutionInfo | None = None
