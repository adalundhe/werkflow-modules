from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeAuthenticationProfileRequest(BaseModel):
    AuthenticationProfileId: StrictStr
    InstanceId: StrictStr
