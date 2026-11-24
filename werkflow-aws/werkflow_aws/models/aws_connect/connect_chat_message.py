from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectChatMessage(BaseModel):
    ContentType: StrictStr
    Content: StrictStr
