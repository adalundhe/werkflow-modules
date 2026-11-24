from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectOutboundRawMessage(BaseModel):
    Subject: StrictStr
    Body: StrictStr
    ContentType: StrictStr
