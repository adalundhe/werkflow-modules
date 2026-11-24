from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexDeleteBotRequest(BaseModel):
    botId: StrictStr
    skipResourceInUseCheck: StrictBool | None = None
