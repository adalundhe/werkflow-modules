from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_completion_report import FSxCompletionReport
from .f_sx_data_repository_task_failure_details import FSxDataRepositoryTaskFailureDetails
from .f_sx_data_repository_task_status import FSxDataRepositoryTaskStatus
from .f_sx_release_configuration import FSxReleaseConfiguration
from .f_sx_tag import FSxTag


class FSxDataRepositoryTask(BaseModel):
    TaskId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    Type: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResourceARN: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    FileSystemId: StrictStr | None = None
    Paths: list[StrictStr] | None = None
    FailureDetails: FSxDataRepositoryTaskFailureDetails | None = None
    Status: FSxDataRepositoryTaskStatus | None = None
    Report: FSxCompletionReport | None = None
    CapacityToRelease: StrictInt | None = None
    FileCacheId: StrictStr | None = None
    ReleaseConfiguration: FSxReleaseConfiguration | None = None
