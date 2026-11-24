from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_filter_rule import DataSyncFilterRule
from .data_sync_manifest_config import DataSyncManifestConfig
from .data_sync_options import DataSyncOptions
from .data_sync_task_report_config import DataSyncTaskReportConfig
from .data_sync_task_schedule import DataSyncTaskSchedule


class DataSyncUpdateTaskRequest(BaseModel):
    TaskArn: StrictStr
    Options: DataSyncOptions | None = None
    Excludes: list[DataSyncFilterRule] | None = None
    Schedule: DataSyncTaskSchedule | None = None
    Name: StrictStr | None = None
    CloudWatchLogGroupArn: StrictStr | None = None
    Includes: list[DataSyncFilterRule] | None = None
    ManifestConfig: DataSyncManifestConfig | None = None
    TaskReportConfig: DataSyncTaskReportConfig | None = None
