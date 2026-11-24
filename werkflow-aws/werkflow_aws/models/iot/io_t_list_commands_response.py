from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_command_summary import IoTCommandSummary


class IoTListCommandsResponse(BaseModel):
    commands: list[IoTCommandSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
