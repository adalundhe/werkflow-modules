from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_log_target_configuration import IoTLogTargetConfiguration


class IoTListV2LoggingLevelsResponse(BaseModel):
    logTargetConfigurations: list[IoTLogTargetConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
