from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteConnectionRequest(BaseModel):
    connectionId: StrictStr
