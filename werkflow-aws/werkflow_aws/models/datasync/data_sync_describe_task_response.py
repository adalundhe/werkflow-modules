from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_filter_rule import DataSyncFilterRule
from .data_sync_manifest_config import DataSyncManifestConfig
from .data_sync_options import DataSyncOptions
from .data_sync_task_report_config import DataSyncTaskReportConfig
from .data_sync_task_schedule import DataSyncTaskSchedule
from .data_sync_task_schedule_details import DataSyncTaskScheduleDetails


class DataSyncDescribeTaskResponse(BaseModel):
    TaskArn: StrictStr | None = None
    Status: StrictStr | None = None
    Name: StrictStr | None = None
    CurrentTaskExecutionArn: StrictStr | None = None
    SourceLocationArn: StrictStr | None = None
    DestinationLocationArn: StrictStr | None = None
    CloudWatchLogGroupArn: StrictStr | None = None
    SourceNetworkInterfaceArns: list[StrictStr] | None = None
    DestinationNetworkInterfaceArns: list[StrictStr] | None = None
    Options: DataSyncOptions | None = None
    Excludes: list[DataSyncFilterRule] | None = None
    Schedule: DataSyncTaskSchedule | None = None
    ErrorCode: StrictStr | None = None
    ErrorDetail: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Includes: list[DataSyncFilterRule] | None = None
    ManifestConfig: DataSyncManifestConfig | None = None
    TaskReportConfig: DataSyncTaskReportConfig | None = None
    ScheduleDetails: DataSyncTaskScheduleDetails | None = None
    TaskMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
