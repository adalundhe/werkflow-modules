from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoSyncRegisterDeviceRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    Platform: Literal['APNS', 'APNS_SANDBOX', 'GCM', 'ADM']
    Token: StrictStr
