from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPForgetDeviceRequest(BaseModel):
    DeviceKey: StrictStr
    AccessToken: StrictStr | None = None
