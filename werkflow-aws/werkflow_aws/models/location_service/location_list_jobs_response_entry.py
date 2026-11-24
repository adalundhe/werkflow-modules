from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .location_job_action_options import LocationJobActionOptions
from .location_job_error import LocationJobError
from .location_job_input_options import LocationJobInputOptions
from .location_job_output_options import LocationJobOutputOptions


class LocationListJobsResponseEntry(BaseModel):
    Action: StrictStr | None = None
    ActionOptions: LocationJobActionOptions | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    Error: LocationJobError | None = None
    InputOptions: LocationJobInputOptions | None = None
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    Name: StrictStr | None = None
    OutputOptions: LocationJobOutputOptions | None = None
    Status: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
