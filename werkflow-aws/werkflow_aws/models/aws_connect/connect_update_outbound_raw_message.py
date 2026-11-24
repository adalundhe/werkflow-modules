from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateOutboundRawMessage(BaseModel):
    Body: StrictStr
    ContentType: StrictStr
