from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteUserRequest(BaseModel):
    ServerId: StrictStr
    UserName: StrictStr
