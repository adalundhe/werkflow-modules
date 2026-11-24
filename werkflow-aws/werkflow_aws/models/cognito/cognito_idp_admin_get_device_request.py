from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminGetDeviceRequest(BaseModel):
    DeviceKey: StrictStr
    UserPoolId: StrictStr
    Username: StrictStr
