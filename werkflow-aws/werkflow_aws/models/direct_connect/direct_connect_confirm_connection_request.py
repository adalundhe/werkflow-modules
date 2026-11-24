from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmConnectionRequest(BaseModel):
    connectionId: StrictStr
