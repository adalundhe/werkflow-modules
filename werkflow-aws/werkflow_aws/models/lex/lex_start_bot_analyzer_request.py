from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexStartBotAnalyzerRequest(BaseModel):
    botId: StrictStr
    analysisScope: Literal['BotLocale']
    localeId: StrictStr | None = None
    botVersion: StrictStr | None = None
