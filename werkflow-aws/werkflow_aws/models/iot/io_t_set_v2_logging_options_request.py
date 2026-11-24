from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_log_event_configuration import IoTLogEventConfiguration


class IoTSetV2LoggingOptionsRequest(BaseModel):
    roleArn: StrictStr | None = None
    defaultLogLevel: Literal['DEBUG', 'INFO', 'ERROR', 'WARN', 'DISABLED'] | None = None
    disableAllLogs: StrictBool | None = None
    eventConfigurations: list[IoTLogEventConfiguration] | None = None
