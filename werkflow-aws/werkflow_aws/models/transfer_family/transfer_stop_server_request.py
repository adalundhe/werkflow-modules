from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferStopServerRequest(BaseModel):
    ServerId: StrictStr
