from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_log_target import IoTLogTarget


class IoTLogTargetConfiguration(BaseModel):
    logTarget: IoTLogTarget | None = None
    logLevel: StrictStr | None = None
