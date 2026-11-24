from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBuildBotLocaleRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
