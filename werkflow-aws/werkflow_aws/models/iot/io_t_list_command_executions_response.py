from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_command_execution_summary import IoTCommandExecutionSummary


class IoTListCommandExecutionsResponse(BaseModel):
    commandExecutions: list[IoTCommandExecutionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
