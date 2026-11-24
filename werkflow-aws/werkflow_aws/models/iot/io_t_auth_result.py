from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_allowed import IoTAllowed
from .io_t_auth_info import IoTAuthInfo
from .io_t_denied import IoTDenied


class IoTAuthResult(BaseModel):
    authInfo: IoTAuthInfo | None = None
    allowed: IoTAllowed | None = None
    denied: IoTDenied | None = None
    authDecision: StrictStr | None = None
    missingContextValues: list[StrictStr] | None = None
