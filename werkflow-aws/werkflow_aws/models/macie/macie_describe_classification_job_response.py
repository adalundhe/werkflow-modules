from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_job_schedule_frequency import MacieJobScheduleFrequency
from .macie_last_run_error_status import MacieLastRunErrorStatus
from .macie_s3_job_definition import MacieS3JobDefinition
from .macie_statistics import MacieStatistics
from .macie_user_paused_details import MacieUserPausedDetails


class MacieDescribeClassificationJobResponse(BaseModel):
    allowListIds: list[StrictStr] | None = None
    clientToken: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    customDataIdentifierIds: list[StrictStr] | None = None
    description: StrictStr | None = None
    initialRun: StrictBool | None = None
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    jobStatus: StrictStr | None = None
    jobType: StrictStr | None = None
    lastRunErrorStatus: MacieLastRunErrorStatus | None = None
    lastRunTime: datetime.datetime | StrictStr | None = None
    managedDataIdentifierIds: list[StrictStr] | None = None
    managedDataIdentifierSelector: StrictStr | None = None
    name: StrictStr | None = None
    s3JobDefinition: MacieS3JobDefinition | None = None
    samplingPercentage: StrictInt | None = None
    scheduleFrequency: MacieJobScheduleFrequency | None = None
    statistics: MacieStatistics | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    userPausedDetails: MacieUserPausedDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
