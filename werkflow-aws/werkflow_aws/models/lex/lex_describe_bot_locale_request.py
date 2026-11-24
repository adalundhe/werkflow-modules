from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotLocaleRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
