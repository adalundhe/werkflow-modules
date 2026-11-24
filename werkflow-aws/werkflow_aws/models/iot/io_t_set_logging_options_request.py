from __future__ import annotations
from pydantic import BaseModel
from .io_t_logging_options_payload import IoTLoggingOptionsPayload


class IoTSetLoggingOptionsRequest(BaseModel):
    loggingOptionsPayload: IoTLoggingOptionsPayload
