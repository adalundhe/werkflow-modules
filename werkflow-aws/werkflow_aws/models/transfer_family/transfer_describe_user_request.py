from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeUserRequest(BaseModel):
    ServerId: StrictStr
    UserName: StrictStr
