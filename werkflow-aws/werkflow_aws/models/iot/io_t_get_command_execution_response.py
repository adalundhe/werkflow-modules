from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_command_execution_result import IoTCommandExecutionResult
from .io_t_command_parameter_value import IoTCommandParameterValue
from .io_t_status_reason import IoTStatusReason


class IoTGetCommandExecutionResponse(BaseModel):
    executionId: StrictStr | None = None
    commandArn: StrictStr | None = None
    targetArn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: IoTStatusReason | None = None
    result: dict[StrictStr, IoTCommandExecutionResult] | None = None
    parameters: dict[StrictStr, IoTCommandParameterValue] | None = None
    executionTimeoutSeconds: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
    timeToLive: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
