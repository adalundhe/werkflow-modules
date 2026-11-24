from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexDeleteBotAliasRequest(BaseModel):
    botAliasId: StrictStr
    botId: StrictStr
    skipResourceInUseCheck: StrictBool | None = None
