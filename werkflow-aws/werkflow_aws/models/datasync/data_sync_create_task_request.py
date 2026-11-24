from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_filter_rule import DataSyncFilterRule
from .data_sync_manifest_config import DataSyncManifestConfig
from .data_sync_options import DataSyncOptions
from .data_sync_tag_list_entry import DataSyncTagListEntry
from .data_sync_task_report_config import DataSyncTaskReportConfig
from .data_sync_task_schedule import DataSyncTaskSchedule


class DataSyncCreateTaskRequest(BaseModel):
    SourceLocationArn: StrictStr
    DestinationLocationArn: StrictStr
    CloudWatchLogGroupArn: StrictStr | None = None
    Name: StrictStr | None = None
    Options: DataSyncOptions | None = None
    Excludes: list[DataSyncFilterRule] | None = None
    Schedule: DataSyncTaskSchedule | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    Includes: list[DataSyncFilterRule] | None = None
    ManifestConfig: DataSyncManifestConfig | None = None
    TaskReportConfig: DataSyncTaskReportConfig | None = None
    TaskMode: Literal['BASIC', 'ENHANCED'] | None = None
