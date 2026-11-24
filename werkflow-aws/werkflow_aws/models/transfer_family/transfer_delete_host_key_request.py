from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteHostKeyRequest(BaseModel):
    ServerId: StrictStr
    HostKeyId: StrictStr
