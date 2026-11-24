from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteSessionRequest(BaseModel):
    InstanceId: StrictStr
    SessionId: StrictStr
