from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminForgetDeviceRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    DeviceKey: StrictStr
