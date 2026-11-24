from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectChatEvent(BaseModel):
    Type: Literal['DISCONNECT', 'MESSAGE', 'EVENT']
    ContentType: StrictStr | None = None
    Content: StrictStr | None = None
