from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchAcceptInboundConnectionRequest(BaseModel):
    ConnectionId: StrictStr
