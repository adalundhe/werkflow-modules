from __future__ import annotations
from pydantic import BaseModel
from .io_t_sig_v4_authorization import IoTSigV4Authorization


class IoTHttpAuthorization(BaseModel):
    sigv4: IoTSigV4Authorization | None = None
