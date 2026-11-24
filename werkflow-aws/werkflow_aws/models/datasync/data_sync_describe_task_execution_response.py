from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .data_sync_filter_rule import DataSyncFilterRule
from .data_sync_manifest_config import DataSyncManifestConfig
from .data_sync_options import DataSyncOptions
from .data_sync_report_result import DataSyncReportResult
from .data_sync_task_execution_files_failed_detail import DataSyncTaskExecutionFilesFailedDetail
from .data_sync_task_execution_files_listed_detail import DataSyncTaskExecutionFilesListedDetail
from .data_sync_task_execution_folders_failed_detail import DataSyncTaskExecutionFoldersFailedDetail
from .data_sync_task_execution_folders_listed_detail import DataSyncTaskExecutionFoldersListedDetail
from .data_sync_task_execution_result_detail import DataSyncTaskExecutionResultDetail
from .data_sync_task_report_config import DataSyncTaskReportConfig


class DataSyncDescribeTaskExecutionResponse(BaseModel):
    TaskExecutionArn: StrictStr | None = None
    Status: StrictStr | None = None
    Options: DataSyncOptions | None = None
    Excludes: list[DataSyncFilterRule] | None = None
    Includes: list[DataSyncFilterRule] | None = None
    ManifestConfig: DataSyncManifestConfig | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EstimatedFilesToTransfer: StrictInt | None = None
    EstimatedBytesToTransfer: StrictInt | None = None
    FilesTransferred: StrictInt | None = None
    BytesWritten: StrictInt | None = None
    BytesTransferred: StrictInt | None = None
    BytesCompressed: StrictInt | None = None
    Result: DataSyncTaskExecutionResultDetail | None = None
    TaskReportConfig: DataSyncTaskReportConfig | None = None
    FilesDeleted: StrictInt | None = None
    FilesSkipped: StrictInt | None = None
    FilesVerified: StrictInt | None = None
    ReportResult: DataSyncReportResult | None = None
    EstimatedFilesToDelete: StrictInt | None = None
    TaskMode: StrictStr | None = None
    FilesPrepared: StrictInt | None = None
    FilesListed: DataSyncTaskExecutionFilesListedDetail | None = None
    FilesFailed: DataSyncTaskExecutionFilesFailedDetail | None = None
    EstimatedFoldersToDelete: StrictInt | None = None
    EstimatedFoldersToTransfer: StrictInt | None = None
    FoldersSkipped: StrictInt | None = None
    FoldersPrepared: StrictInt | None = None
    FoldersTransferred: StrictInt | None = None
    FoldersVerified: StrictInt | None = None
    FoldersDeleted: StrictInt | None = None
    FoldersListed: DataSyncTaskExecutionFoldersListedDetail | None = None
    FoldersFailed: DataSyncTaskExecutionFoldersFailedDetail | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
