from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_job_schedule_frequency import MacieJobScheduleFrequency
from .macie_s3_job_definition import MacieS3JobDefinition


class MacieCreateClassificationJobRequest(BaseModel):
    clientToken: StrictStr
    jobType: Literal['ONE_TIME', 'SCHEDULED']
    name: StrictStr
    s3JobDefinition: MacieS3JobDefinition
    allowListIds: list[StrictStr] | None = None
    customDataIdentifierIds: list[StrictStr] | None = None
    description: StrictStr | None = None
    initialRun: StrictBool | None = None
    managedDataIdentifierIds: list[StrictStr] | None = None
    managedDataIdentifierSelector: Literal['ALL', 'EXCLUDE', 'INCLUDE', 'NONE', 'RECOMMENDED'] | None = None
    samplingPercentage: StrictInt | None = None
    scheduleFrequency: MacieJobScheduleFrequency | None = None
    tags: dict[StrictStr, StrictStr] | None = None
