from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexGenerateBotElementRequest(BaseModel):
    intentId: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
