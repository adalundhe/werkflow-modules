from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetFederationTokenRequest(BaseModel):
    InstanceId: StrictStr
