from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexDeleteBotVersionRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    skipResourceInUseCheck: StrictBool | None = None
