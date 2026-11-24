from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteOutboundConnectionRequest(BaseModel):
    ConnectionId: StrictStr
