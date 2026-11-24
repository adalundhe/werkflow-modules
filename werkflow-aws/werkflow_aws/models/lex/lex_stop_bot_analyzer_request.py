from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexStopBotAnalyzerRequest(BaseModel):
    botId: StrictStr
    botAnalyzerRequestId: StrictStr
