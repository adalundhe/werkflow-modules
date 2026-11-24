from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeServerRequest(BaseModel):
    ServerId: StrictStr
