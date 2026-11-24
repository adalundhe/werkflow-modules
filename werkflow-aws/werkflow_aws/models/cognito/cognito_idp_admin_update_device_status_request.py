from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminUpdateDeviceStatusRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    DeviceKey: StrictStr
    DeviceRememberedStatus: Literal['remembered', 'not_remembered'] | None = None
