from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeUserRequest(BaseModel):
    UserId: StrictStr
    InstanceId: StrictStr
