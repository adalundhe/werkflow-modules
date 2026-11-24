from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDescribeUserRequest(BaseModel):
    BrokerId: StrictStr
    Username: StrictStr
