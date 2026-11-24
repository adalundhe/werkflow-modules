from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_log_event_configuration import IoTLogEventConfiguration


class IoTGetV2LoggingOptionsResponse(BaseModel):
    roleArn: StrictStr | None = None
    defaultLogLevel: StrictStr | None = None
    disableAllLogs: StrictBool | None = None
    eventConfigurations: list[IoTLogEventConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
