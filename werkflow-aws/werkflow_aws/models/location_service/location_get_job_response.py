from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_job_action_options import LocationJobActionOptions
from .location_job_error import LocationJobError
from .location_job_input_options import LocationJobInputOptions
from .location_job_output_options import LocationJobOutputOptions


class LocationGetJobResponse(BaseModel):
    Action: StrictStr | None = None
    ActionOptions: LocationJobActionOptions | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    Error: LocationJobError | None = None
    ExecutionRoleArn: StrictStr | None = None
    InputOptions: LocationJobInputOptions | None = None
    JobArn: StrictStr | None = None
    JobId: StrictStr | None = None
    Name: StrictStr | None = None
    OutputOptions: LocationJobOutputOptions | None = None
    Status: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
