from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteInterconnectRequest(BaseModel):
    interconnectId: StrictStr
