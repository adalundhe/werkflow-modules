from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteUserRequest(BaseModel):
    InstanceId: StrictStr
    UserId: StrictStr
