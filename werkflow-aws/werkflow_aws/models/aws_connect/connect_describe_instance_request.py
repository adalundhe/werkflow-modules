from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeInstanceRequest(BaseModel):
    InstanceId: StrictStr
