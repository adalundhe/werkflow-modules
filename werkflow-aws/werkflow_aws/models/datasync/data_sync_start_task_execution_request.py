from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_filter_rule import DataSyncFilterRule
from .data_sync_manifest_config import DataSyncManifestConfig
from .data_sync_options import DataSyncOptions
from .data_sync_tag_list_entry import DataSyncTagListEntry
from .data_sync_task_report_config import DataSyncTaskReportConfig


class DataSyncStartTaskExecutionRequest(BaseModel):
    TaskArn: StrictStr
    OverrideOptions: DataSyncOptions | None = None
    Includes: list[DataSyncFilterRule] | None = None
    Excludes: list[DataSyncFilterRule] | None = None
    ManifestConfig: DataSyncManifestConfig | None = None
    TaskReportConfig: DataSyncTaskReportConfig | None = None
    Tags: list[DataSyncTagListEntry] | None = None
