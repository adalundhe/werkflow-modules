from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociateConnectionWithLagRequest(BaseModel):
    connectionId: StrictStr
    lagId: StrictStr
