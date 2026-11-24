from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMEnableMFADeviceRequest(BaseModel):
    UserName: StrictStr
    SerialNumber: StrictStr
    AuthenticationCode1: StrictStr
    AuthenticationCode2: StrictStr
