from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_jobs_data_command_parameter_value import IoTJobsDataCommandParameterValue


class IoTJobsDataStartCommandExecutionRequest(BaseModel):
    targetArn: StrictStr
    commandArn: StrictStr
    parameters: dict[StrictStr, IoTJobsDataCommandParameterValue] | None = None
    executionTimeoutSeconds: StrictInt | None = None
    clientToken: StrictStr | None = None
