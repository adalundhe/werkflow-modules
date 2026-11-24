from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotAliasRequest(BaseModel):
    botAliasId: StrictStr
    botId: StrictStr
