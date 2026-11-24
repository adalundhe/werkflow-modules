from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeactivateMFADeviceRequest(BaseModel):
    SerialNumber: StrictStr
    UserName: StrictStr | None = None
