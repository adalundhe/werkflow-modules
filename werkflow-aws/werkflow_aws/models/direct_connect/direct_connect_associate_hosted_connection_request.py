from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociateHostedConnectionRequest(BaseModel):
    connectionId: StrictStr
    parentConnectionId: StrictStr
