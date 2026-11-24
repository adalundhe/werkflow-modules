from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexListBotAnalyzerHistoryRequest(BaseModel):
    botId: StrictStr
    localeId: StrictStr | None = None
    botVersion: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
