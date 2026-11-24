from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetDeviceRequest(BaseModel):
    DeviceKey: StrictStr
    AccessToken: StrictStr | None = None
