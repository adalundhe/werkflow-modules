from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchRejectInboundConnectionRequest(BaseModel):
    ConnectionId: StrictStr
