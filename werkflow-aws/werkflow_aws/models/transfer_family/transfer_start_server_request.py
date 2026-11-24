from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferStartServerRequest(BaseModel):
    ServerId: StrictStr
