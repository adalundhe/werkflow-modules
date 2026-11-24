from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexListRecommendedIntentsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    botRecommendationId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
