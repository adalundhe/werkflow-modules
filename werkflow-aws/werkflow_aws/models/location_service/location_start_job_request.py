from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_job_action_options import LocationJobActionOptions
from .location_job_input_options import LocationJobInputOptions
from .location_job_output_options import LocationJobOutputOptions


class LocationStartJobRequest(BaseModel):
    Action: Literal['ValidateAddress']
    ExecutionRoleArn: StrictStr
    InputOptions: LocationJobInputOptions
    OutputOptions: LocationJobOutputOptions
    ClientToken: StrictStr | None = None
    ActionOptions: LocationJobActionOptions | None = None
    Name: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
