from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexListBotRecommendationsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
