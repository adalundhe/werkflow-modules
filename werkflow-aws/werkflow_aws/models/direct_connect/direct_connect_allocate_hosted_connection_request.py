from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectAllocateHostedConnectionRequest(BaseModel):
    connectionId: StrictStr
    ownerAccount: StrictStr
    bandwidth: StrictStr
    connectionName: StrictStr
    vlan: StrictInt
    tags: list[DirectConnectTag] | None = None
