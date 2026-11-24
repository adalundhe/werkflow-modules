from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .io_t_log_target import IoTLogTarget


class IoTSetV2LoggingLevelRequest(BaseModel):
    logTarget: IoTLogTarget
    logLevel: Literal['DEBUG', 'INFO', 'ERROR', 'WARN', 'DISABLED']
