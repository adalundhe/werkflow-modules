from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeHostKeyRequest(BaseModel):
    ServerId: StrictStr
    HostKeyId: StrictStr
