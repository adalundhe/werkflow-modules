from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDisassociateConnectionsFromResiliencyGroupRequest(BaseModel):
    connectionIdentifiers: list[StrictStr]
    resiliencyGroupId: StrictStr
    clientToken: StrictStr | None = None
