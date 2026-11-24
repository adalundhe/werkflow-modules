from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDisassociateConnectionFromLagRequest(BaseModel):
    connectionId: StrictStr
    lagId: StrictStr
