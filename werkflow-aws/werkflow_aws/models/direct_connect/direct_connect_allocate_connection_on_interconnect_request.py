from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectAllocateConnectionOnInterconnectRequest(BaseModel):
    bandwidth: StrictStr
    connectionName: StrictStr
    ownerAccount: StrictStr
    interconnectId: StrictStr
    vlan: StrictInt
